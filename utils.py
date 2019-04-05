def clamp(val: int, low: int, high: int) -> int:
    if val < low:
        return low
    elif val > high:
        return high
    else:
        return val
