def convert_input_to_list_and_tuple(input):
    values = input.split(',')
    return values, tuple(values)

print(convert_input_to_list_and_tuple('1,2,3,4,5'))