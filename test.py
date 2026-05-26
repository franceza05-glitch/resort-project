def find_numbers(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))
    return ','.join(result)

# Call the function with specific start and end values
print(find_numbers(100, 200))

