def check(f, a, b):
    left, right = a, b
    intervals = []
    while left < right:
        left_value = f(left)
        if left + 0.5 >= right:
            new_left = right
            right_value = f(new_left)
        else:
            new_left = left + 0.5
            right_value = f(new_left)
        if left_value * right_value <= 0:
            intervals.append([left, new_left])
        left = new_left
    return intervals

