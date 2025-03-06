# TODO
from cs50 import get_string

# Prompt user for input
text = get_string("Text: ")

# Count number of letters, words and sentences.
letters = 0
for i in text:
    if i.isalpha():
        letters += 1

words = len(text.split())

sentences = text.count(".") + text.count("!") + text.count("?")


L = (letters / words) * 100.0
S = (sentences / words) * 100.0

# Coleman-Liau Index
index = 0.0588 * L - 0.296 * S - 15.8

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade", round(index))
