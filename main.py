"""
Chapter 1 - Can a Computer Learn y = 2x?

Bro: I know the answer.
Computer: Then tell me.
Bro: Nope. You learn it.

Let's see what happens.
"""


print("Bro: Okay computer, here is your first challenge.")
print("Computer: Please tell me you are giving me more than zero information.")
print("Bro: Nope. Just examples.")
print()


# Training examples
training_data = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]


print("Bro: These are your examples:")
print()

for x, y in training_data:
    print(f"Input: {x}  ->  Expected Output: {y}")


print()

print("Computer: Hmm...")
print("Computer: I see numbers, but I have absolutely no idea what they mean.")
print("Bro: Perfect. That means we can start learning.")