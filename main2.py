# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

from collections import Counter

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(Counter(word) != Counter(anagram)):
        return False
    else:
        return True

while True:
    word = (input("Enter the first word: ").lower())
    if not word.isalpha():
        print("Please enter only alphabetical words: ")
        continue
    else:
        break

while True:
    anagram = (input("Enter the second word: ").lower())
    if not anagram.isalpha():
        print("Please enter only alphabetical words: ")
        continue
    else:
        break
            
find_anagram(word, anagram)

