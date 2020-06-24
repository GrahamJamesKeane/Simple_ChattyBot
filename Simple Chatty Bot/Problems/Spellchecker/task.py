dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()
correct = False
for i in dictionary:
    if word == i:
        correct = True
print("Correct" if correct else "Incorrect")
