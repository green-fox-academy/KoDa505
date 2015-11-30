#def forditas(theword):
#    forditott = ''
#    for i in theword:
#        forditott = i + forditott
#    return theword + forditott

#print(forditas("pear"))


def search_palindromes(text):
    words = text.split()
    palindromes = []    
    for word in words:
        i = 0
        backward = word[::-1]
        while i < len(word)-1:
            j = 0
            while j < len(backward)-1:
                if word[i] == backward[j]:
                    palindrome = palindrome + word[i]
                    i += 1
                    j += 1
                else:
                    j += 1
#            palindromes = palindromes + palindrome
            i += 1

print(search_palindromes('never ever'))
