

def search_palindromes(text):
    words = text.split()
    palindrome = []
    for word in words:
        for i in range(len(word)-1):
            for j in range(i+1,len(word)):
                part = word[i:j+1]
                if part == part[::-1] and len(part)>= 3:
                    palindrome.append(part)
    return palindrome

print(search_palindromes('never ever'))
print(search_palindromes('indul a gorog aludni'))
print(search_palindromes('dad doodle never wherever'))
print(search_palindromes(''))
