import hashlib
import time

_hashtable = hashlib
hashtable = {}
for index, value in _hashtable.__dict__.items():
    if callable(value):
        print(f"Added {index} to hashtable")
        hashtable[index] = value

correctalgo = False
while not correctalgo:
    algorithm = input("Enter an algorithm to encode with: ")
    if algorithm not in hashlib.algorithms_guaranteed:
        print("Invalid algorithm! Please type a correct algorithm")
    else:
        correctalgo = True

text = input("Enter text to encode with algorithm \"" + algorithm + "\": ")
time.sleep(1)
encodedtext = hashtable[algorithm](text.encode()).hexdigest()

print(f"Your hash for the text \"{text}\" is:\n{encodedtext}")
time.sleep(1)
quit()