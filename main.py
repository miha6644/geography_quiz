countries = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}
correct = 0
incorrect = 0

for k in countries:                 # k stands for "key" in the dictionary, while the other thing is its "value" (v)
    capital = countries[k]
    print("\nWhat is the capital of:", k)               # \n starts the string in a new line
    answer = input("Please type your answer: ")
    if answer.lower().upper() == capital.lower().upper():
        print("Your answer is correct!")
        correct += 1
    else:
        print("Sorry the answer is", capital + ".")
        incorrect += 1
print("Correct answers:", correct, "/ Incorrect answers:", incorrect)
