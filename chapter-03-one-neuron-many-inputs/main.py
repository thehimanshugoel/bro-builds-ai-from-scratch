from neuron import Neuron
from loss import calculate_loss


# Training data:
# [Experience, Education] -> Salary
training_data = [
    ([2, 1], 5),
    ([4, 2], 10),
    ([6, 3], 15),
    ([8, 4], 20),
]


print("Training Data\n")

for inputs, actual in training_data:
    print(f"{inputs} -> {actual}")


neuron = Neuron()


print("\nInitial Neuron")
print(f"Weights: {neuron.weights}")
print(f"Bias: {neuron.bias:.2f}")


print("\nPredictions\n")

for inputs, actual in training_data:

    prediction = neuron.predict(inputs)

    loss = calculate_loss(prediction, actual)

    print(f"Inputs     : {inputs}")
    print(f"Prediction : {prediction:.2f}")
    print(f"Actual     : {actual}")
    print(f"Loss       : {loss:.2f}")
    print("-" * 35)


test_input = [10, 5]

print("\nTest Prediction")
print(f"Input: {test_input}")
print(f"Prediction: {neuron.predict(test_input):.2f}")