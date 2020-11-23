

#Input a letter combination.
print("Input letter combination")
inputComb = input()
print(inputComb)

#Understand how this works
#It sorts both words into alphabetically ordered lowercase letters and checks if they match.
def anagrams( s1 , s2 ):
    s1 = sorted(s1.lower())
    s2 = sorted(s2.lower())
    return s1 == s2
#Checks all lines in dictionary.txt and checks for inputsorted and line->word matches.words_alpha.txt
def find_all_anagrams( inputComb ):
    anagram_list = []
    with open('dictionary.txt', 'r') as fileObject:
        for line in fileObject:
            word = line.strip()
            if anagrams (inputComb, word):
                anagram_list.append(word)
    return anagram_list

print(find_all_anagrams(inputComb))