my_file = open('texts/encoded_zen_lines.txt')
output_file = open('decoded_zen_lines.txt', 'a')

text = my_file.read()
my_file.close()

lines = text.split("\n")


decoded = []
for line in lines:
    words = line.split(" ")
    decodedline = []
    for word in words:
        decodedword = ""
        for letter in word:
            decodedword += chr(ord(letter)-1)
        decodedline.append(decodedword)
    decoded.append(" ".join(decodedline))

decodedtext = "\n".join(decoded)

output_file.write(decodedtext)
output_file.close()

print(decodedtext)
