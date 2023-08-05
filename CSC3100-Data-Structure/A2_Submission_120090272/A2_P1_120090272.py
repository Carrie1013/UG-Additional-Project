def twoSum():
    n, t = input().split(' ')
    n = int(n)
    t = int(t)

    nums = input().split(' ')
    nums = [int(i) for i in nums]

    if t/2 == int(t/2) and nums.count(int(t/2)) == 2:
        ind_1 = nums.index(int(t/2))
        ind_2 = nums.index(int(t/2), ind_1+1, n)
        print(ind_1+1, ind_2+1)
        return

    new_nums = list(set(nums))
    n = len(new_nums)
    number_set = set()

    for number in [i-t/2 for i in new_nums]:
        if abs(number) in number_set:
            tgt_num = number
            break
        else:
            number_set.add(abs(number))

    ind_1 = nums.index(int(t/2+tgt_num))+1
    ind_2 = nums.index(int(t/2-tgt_num))+1

    print(min(ind_1,ind_2),max(ind_1,ind_2))

twoSum()