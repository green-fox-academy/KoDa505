def rot13(message):
    first = "ABCDEFGHIJKLMabcdefghijklm"
    second = "NOPQRSTUVWXYYnopqrstuvwxyz"
    reversed=""
    for i in message:
        if i in first:
            reversed = reversed + chr(ord(i) + 13)
        elif i in second:
            reversed = reversed + chr(ord(i) - 13)
        else:
            reversed = reversed + i
    return reversed

print(rot13("URyyb13"))
