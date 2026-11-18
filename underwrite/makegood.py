def remaining(slots, booking):
    index = {row['id']: row['capacity'] for row in slots}
    for row in booking:
        index[row['slot']] -= 1
    if min(index.values(), default=0) < 0:
        raise ValueError('登记的预留超过节目容量')
    return index
