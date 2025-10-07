word = input("Enter input: ")
i = len(word) - 1
new_word
while i >= 0:
    new_word = new_word + word[i]
    i = i - 1
print(new_word)