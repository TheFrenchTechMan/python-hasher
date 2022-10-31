import hashlib
import time

_hashtable = hashlib
hashtable = {}
for index, value in _hashtable.__dict__.items():
    if callable(value):
        hashtable[index] = value

correctAlgorithm = False
while not correctAlgorithm:
    algorithm = input("Enter an algorithm to encode with: ")
    if algorithm not in hashlib.algorithms_guaranteed:
        print("Invalid algorithm! Please type a correct algorithm.")
    else:
        correctAlgorithm = True

text = input("Enter text to encode with algorithm \"" + algorithm + "\": ")

encodedtext = hashtable[algorithm](text.encode()).hexdigest()

print(f"\nYour hash for the text \"{text}\" is:\n\n{encodedtext}\n")
quit()