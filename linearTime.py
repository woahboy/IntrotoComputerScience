def proc1(input_list): # linear time!
    maximum = None
    for element in input_list :
        if not maximum or maximum < element:
            maximum = element
    return maximum

def proc2(input_list): # linear time!
    sum = 0
    while len(input_list) > 0:
        sum = sum + input_list[0]   # Assume input_list[0] is constant time
        input_list = input_list[1:]  # Assume input_list[1:] is constant time
    return sum

def proc3(input_list): # not linear
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i] == input_list[j] and i != j:
                return False
    return True
