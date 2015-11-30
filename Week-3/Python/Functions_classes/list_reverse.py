def reverse(in_list):
    output = []
    i = len(in_list) - 1
    while i >= 0 :
        output.append(in_list[i])
        i -= 1
    return output

output = reverse([1, 3, 4, 7])
print(output)
