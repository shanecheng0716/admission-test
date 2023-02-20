


def find_max(list_num):
    max_num = list_num[0]
    for x in range(len(list_num)):
        if max_num < list_num[x]:
            max_num = list_num[x]
    return(max_num)
    
    
def find_position(list_num, target):
    find = -1
    for x in range(len(list_num)):
        if list_num[x] == target:
            find = x
            break
    return find


print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1



def count(input):
    intput_dic = {}
    for x in range(len(input)):
        num = 0
        for y in range(x, len(input)):
            if input[x] == input[y]:
                num += 1
        if intput_dic.get(input[x], 0) == 0:
            intput_dic[input[x]] = num
    return intput_dic
        
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}



def group_by_key(input):
    f_dic = {}
    for x in range(len(input)):
        if f_dic.get(input[x].get("key"), 0) == 0:
            f_dic[input[x].get("key")] = input[x].get("value")
        else:
            f_dic[input[x].get("key")] = f_dic[input[x].get("key")]+input[x].get("value")

    return f_dic
input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
