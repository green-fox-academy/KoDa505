my_file = open("texts/duplicated_chars.txt")
out_file = open("singlicated_chars.txt", "w")

lines = my_file.readlines()

my_file.close()


decoded = ""
for line in lines:
    text2  = ""
    for i in range(0, len(line), 2):
        text2 = text2 + line[i]
    decoded = decoded + text2


out_file.write(decoded)
out_file.close()
