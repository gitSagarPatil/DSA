def binary_search(input_list, item):
    begin_index = 0
    end_index = len(input_list) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = input_list[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

input_list_1 = [2,4,5,6,7,7,8,9,9,14,14,23,26,59]
item_1 = 14
input_list_2 = [2,6,15,16,33,37,58,60,63,64,64,74,82,99]
item_2 = 1

print(binary_search(input_list=input_list_1, item=item_1))
print(binary_search(input_list=input_list_2, item=item_2))