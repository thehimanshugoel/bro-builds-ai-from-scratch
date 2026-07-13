from neuron import Neuron
from loss import calculate_loss

training_data = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]

print("Training Data")

for x, y in training_data:
    print(f"Input: {x} -> Expected Output: {y}")


neuron = Neuron()

print("\nInitial neuron state:")
print(f"Weight: {neuron.weight:.2f}")
print(f"Bias: {neuron.bias:.2f}")

print("\nPredictions:")

for x, y in training_data:
    prediction = neuron.predict(x)
    loss = calculate_loss(prediction, y)

    print(
        f"Input: {x}, "
        f"Prediction: {prediction:.2f}, "
        f"Actual: {y}, "
        f"Loss: {loss:.2f}"
    )