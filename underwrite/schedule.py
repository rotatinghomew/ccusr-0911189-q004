from collections import Counter


def planned(breaks, contracts):
    names = {row['donor'] for row in contracts}
    if any(row['end'] <= row['start'] or row['donor'] not in names for row in breaks):
        raise ValueError('鸣谢安排缺少有效约定或时段')
    return dict(Counter(row['donor'] for row in breaks))
