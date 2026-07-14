from neuron import Neuron
from loss import calculate_loss


training_data = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]


print("Training data:")

for x, y in training_data:
    print(f"{x} -> {y}")


neuron = Neuron()


print("\nInitial neuron:")
print(f"Weight: {neuron.weight:.2f}")
print(f"Bias: {neuron.bias:.2f}")


for epoch in range(100):

    total_loss = 0

    for x, y in training_data:

        prediction = neuron.predict(x)

        loss = calculate_loss(prediction, y)

        total_loss += loss

        neuron.learn(x, y, prediction)


    if epoch % 10 == 0:
        print(
            f"Epoch {epoch}, Loss: {total_loss:.2f}"
        )


print("\nFinal model:")
print(f"y = {neuron.weight:.2f}x + {neuron.bias:.2f}")


test_input = 10

print(
    f"\nPrediction for {test_input}: "
    f"{neuron.predict(test_input):.2f}"
)