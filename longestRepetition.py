# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(input_list):
    best_element = None
    length = 0
    current_element = None
    current_length = 0
    for element in input_list:
        if current_element != element:
            current_element = element
            current_length = 1
        else:
            current_length += 1
        if current_length > length:
            best_element = current_element
            length = current_length
    return best_element

# def longest_repetition(List):
#     Max = 0
#     count = 0
#     choice = None
#     if List:
#         choice = List[0]
#     for i in range(len(List)):
#         try:
#             if List[i] == List[i+1]:
#                 count += 1
#             else:
#                 if count > Max:
#                     Max = count
#                     choice = List[i]
#                 count = 0
#         except:
#             if count > Max:
#                 choice = List[i]
#             return choice


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3
print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b
print longest_repetition([1,2,3,4,5])
# 1
print longest_repetition([])
# None
print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
# [2,2]
print longest_repetition([2, 2, 3, 3, 3])
# 3
