from .airlog import minutes
from .makegood import remaining
from .schedule import planned


def report(data):
    return {'scheduled': planned(data['breaks'], data['contracts']), 'logs':minutes(data['logs']),
            'free':remaining(data['slots'], data['booking'])}
