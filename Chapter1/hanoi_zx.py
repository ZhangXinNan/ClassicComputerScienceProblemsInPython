
tower_a = []
tower_b = []
tower_c = []


def print_tower(tower):
    print(tower)
    '''
    if len(tower) < 1:
        print(tower)
    for t in tower:
        print(t)
    '''


def hanoi(begin, end, temp, n):
    print("**{}** A:{}, B:{}, C:{}".format(n, tower_a, tower_b, tower_c))
    if n == 1:
        end.append(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


if __name__ == '__main__':
    num_discs = 4
    # 数字越大，代表盘子越小，放在越上边
    tower_a = [i for i in range(1, num_discs+1)]
    '''
    for n in range(1, num_discs + 1):
        tower_a.append(''.join(['T' for _ in range(n)]))
    '''
    print("-----start-----")
    print_tower(tower_a)
    print_tower(tower_b)
    print_tower(tower_c)
    hanoi(tower_a, tower_b, tower_c, num_discs)
    print("-----end-----")
    print_tower(tower_a)
    print_tower(tower_b)
    print_tower(tower_c)
