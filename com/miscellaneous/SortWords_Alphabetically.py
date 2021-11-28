# Sorting words alphabetically

text = input('Please enter sentence: ')

words = text.split()

words.sort()

print("The sorted words are:")
for word in words:
    print(word, end=" ")

print("\nWords at 0 index before sort: ", text[0])
print("\nWords at 0 index after sort: ", words[0])

# i/p: python programming language
# o/p: language programming python
