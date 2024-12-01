def even_squares(limit):
    result = []
    i = 0
    while i < limit:
        if i % 2 == 0:
            result.append(i ** 2)
        i += 1
    return result

# Call the function and print the result
print(even_squares(11))
