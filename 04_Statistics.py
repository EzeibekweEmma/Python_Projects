def get_nums():
    nums = []
    num_of_nums = int(input("How many numbers do you want to input: "))

    for i in range(num_of_nums):
        user_num = int(input("Enter the number: "))
        nums.append(user_num)

    return nums


def mean(list_of_nums):

    total = 0
    len_of_num = len(list_of_nums)

    for i in range(len_of_num):
        total += list_of_nums[i]

    ans = total / len_of_num
    return "mean = {:.2f}".format(ans)


def get_range(list_of_nums):
    ans = max(list_of_nums) - min(list_of_nums)
    return "Range = {:.2f}".format(ans)


def middle_num(list_of_nums):
    list_of_nums.sort()
    index = int((len(list_of_nums) / 2))
    if len(list_of_nums) % 2 == 0:
        mid_nums = list_of_nums[index] + list_of_nums[index - 1]
        ans = mid_nums / 2
    else:
        ans = list_of_nums[index]

    return "Middle Number = {}".format(ans)


def mode(list_of_nums):
    obj_of_high_nums = {}
    highest_num = 0
    mode_num = None

    for i in range(len(list_of_nums)):
        if list_of_nums[i] == list_of_nums[i - 1]:
            obj_of_high_nums[list_of_nums[i]] = [list_of_nums[i]]

    for i in range(len(list_of_nums)):
        if list_of_nums[i] == list_of_nums[i - 1]:
            obj_of_high_nums[list_of_nums[i]].append(list_of_nums[i])

    for i in obj_of_high_nums:
        if highest_num < len(obj_of_high_nums[i]):
            highest_num = len(obj_of_high_nums[i])
            mode_num = obj_of_high_nums[i][0]

    return "Mode Number = {}".format(mode_num)


list_of_num = [2, 4, 5, 6, 6, 7, 7, 7, 6, 5, 6, 2, 4, 6]
mode_dic = {}

for i in list_of_num:
    if i in mode_dic:
        mode_dic[i] += 1
    else:
        mode_dic[i] = 1


max_mode_dic = max(mode_dic.values())
main_mode = []
for i, j in mode_dic.items():
    if j == max_mode_dic:
        main_mode.append(i)

print(main_mode[0])
# nums = get_nums()
#
# print(mean(nums))
# print(get_range(nums))
# print(middle_num(nums))
# print(mode(nums))
