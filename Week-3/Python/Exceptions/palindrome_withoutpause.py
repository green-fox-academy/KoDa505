

def is_palindrome(aword):
    return aword == aword[::-1] and len(aword) >= 3



def search_palindromes(text):
    words = text.split()
    palindrome = []
    for word in words:
        for i in range(len(word)-1):
            for j in range(i+1,len(word)):
                part = word[i:j+1]
                if is_palindrome(part):
                    palindrome.append(part)
    return palindrome

def joint(text):
    replaced = ''
    for i in text:
        if i == ' ':
            replaced = replaced + ''
        else:
            replaced = replaced + i
    return replaced


print(search_palindromes('never ever'))
print(search_palindromes('indul a gorog aludni'))
print(search_palindromes('dad doodle never wherever'))
print(search_palindromes(''))

print(search_palindromes(joint('indul a gorog aludni')))
