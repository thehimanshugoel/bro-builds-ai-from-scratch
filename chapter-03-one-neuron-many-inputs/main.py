from neuron import Neuron
from loss import calculate_loss


training_data = [
    ([2, 1], 5),
    ([4, 2], 10),
    ([6, 3], 15),
    ([8, 4], 20),
]


print("Training Data\n")

for inputs, actual in training_data:
    print(f"{inputs} -> {actual}")


# We have two input features
neuron = Neuron(num_inputs=2)


print("\nInitial Neuron")
print(f"Weights: {neuron.weights}")
print(f"Bias: {neuron.bias:.2f}")


for epoch in range(100):

    total_loss = 0

    for inputs, actual in training_data:

        prediction = neuron.predict(inputs)

        loss = calculate_loss(prediction, actual)

        total_loss += loss

        neuron.learn(inputs, actual, prediction)

    if epoch % 10 == 0:

        print(
            f"Epoch {epoch:3} | "
            f"Loss: {total_loss:.2f} | "
            f"Weights: {[round(w, 2) for w in neuron.weights]} | "
            f"Bias: {neuron.bias:.2f}"
        )


print("\nFinal Model")

print(
    f"Prediction = "
    f"{neuron.weights[0]:.2f}*x1 + "
    f"{neuron.weights[1]:.2f}*x2 + "
    f"{neuron.bias:.2f}"
)


print("\nTesting\n")

test_data = [
    [10, 5],
    [3, 2],
    [7, 4],
]

for inputs in test_data:
    prediction = neuron.predict(inputs)
    print(f"{inputs} -> {prediction:.2f}")