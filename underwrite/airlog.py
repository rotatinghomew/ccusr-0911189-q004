from collections import defaultdict


def minutes(logs):
    result = defaultdict(int)
    for row in logs:
        duration = row['end'] - row['start']
        if duration <= 0 or row['state'] not in {'broadcast', 'muted', 'unknown'}:
            raise ValueError('实况凭证的状态或区间不合法')
        result[(row['station'], row['region'], row['state'])] += duration
    return [{'station': key[0], 'region': key[1], 'state': key[2], 'minutes': total}
            for key, total in sorted(result.items())]
