import hashlib

algorithms = ', '.join((list(hashlib.algorithms_guaranteed)))

_hashtable = hashlib
hashtable = {}
for index, value in _hashtable.__dict__.items():
    if callable(value):
        hashtable[index] = value

print("")
print("Available algorithms: " + algorithms)
print("")

correctAlgorithm = False
while not correctAlgorithm:
    algorithm = input("Enter an algorithm to hash with: ")
    if algorithm not in hashlib.algorithms_guaranteed:
        print("Invalid algorithm! Please type a correct algorithm.")
    else:
        correctAlgorithm = True

text = input("Enter text to hash with algorithm \"" + algorithm + "\": ")

encodedtext = hashtable[algorithm](text.encode()).hexdigest()

print(f"\nYour hash for the text \"{text}\" is:\n\n{encodedtext}\n")

quit()