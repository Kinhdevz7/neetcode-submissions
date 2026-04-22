def add_two_numbers() -> int:
    input_string = input("Type 2 numbers separated by ,")
    string_list = input_string.split(",")
    int_list = []
    for s in string_list:
        int_list.append(int(s))

    return sum(int_list)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
