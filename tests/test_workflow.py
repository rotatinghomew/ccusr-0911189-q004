import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from underwrite.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'underwrite', 'ledger', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_week_keeps_plan_separate_from_logs(self):
        output = report(self.data)
        self.assertEqual(output['scheduled'], {'D1':1,'D2':1})
        self.assertEqual(output['free'], {'late':1,'night':1})
        self.assertIn({'station':'FM','region':'east','state':'muted','minutes':3}, output['logs'])

    def test_cap_rejects_overbooking(self):
        self.data['booking'] *= 3
        with self.assertRaises(ValueError):
            report(self.data)
