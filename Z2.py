word = input()
vowels = "aeiou"
vowels_count = 0
consonants_count = 0

for letter in word:
    if letter in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print("гласных:", vowels_count)
print("согласных:", consonants_count)

for vowel in vowels:
    count = word.count(vowel)

    if count == 0:
        print(vowel, False)
    else:
        print(vowel, count)