def count_letters(input_str):
    output = {}
    if len(input_str) > 0:
        for char in input_str:
            if char not in output:
                output[char] = 1
            else:
                output[char] += 1
    return output
