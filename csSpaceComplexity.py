def do_a_couple_things(n):
    my_list = [] # 1
    my_second_list = [0] * 26 #1

    for _ in range(n): # n
        my_list.append("lambda") # 1
        print(my_second_list[n % 25]) 
    return my_list