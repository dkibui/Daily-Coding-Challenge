def climb_Stairs(n):
    if n <= 1:
        return 1
    pre_path = 1
    cur_path = 1
    for i in range(2, n + 1):
        one_step = cur_path
        two_steps = pre_path
        pre_path = cur_path
        cur_path = one_step + two_steps
    return cur_path
