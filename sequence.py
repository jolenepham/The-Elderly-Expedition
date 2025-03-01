import random
import time

# get sequence length form the user
print(" This game is designed to help your memory.\n First, type a number for the length of the sequence.\n Then, you will have 10 seconds to memorize that sequence.\n Finally, you will be prompted to enter those numbers, one at a time.\n Good Luck!\n")
length = input("Enter the number of digits you want to guess: ")
length = int(length)

# create random sequence
sequence = []
for i in range(0, length):
    sequence.append(random.randint(0,9))
print(sequence)

# show the sequence for 10 seconds
time.sleep(10)

# hide the sequence
for i in range (0,50):
    print(' ')

# check if the inputted sequence matches
for i in range(0, length):
    print('Enter the number: ')
    num = int(input())
    if (num == sequence[i]):
        print("Correct!")
    else:
        print("Try Again.")
        break
print ("The sequence was", sequence)