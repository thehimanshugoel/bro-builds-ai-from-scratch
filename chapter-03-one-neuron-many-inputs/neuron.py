import random


class Neuron:

    def __init__(self, num_inputs):

        # One random weight for each input
        self.weights = [
            random.uniform(-1, 1)
            for _ in range(num_inputs)
        ]

        self.bias = random.uniform(-1, 1)

    def predict(self, inputs):

        prediction = self.bias

        for x, w in zip(inputs, self.weights):
            prediction += x * w

        return prediction

    def learn(self, inputs, actual, prediction, learning_rate=0.01):

        error = actual - prediction

        # Update every weight
        for i in range(len(self.weights)):
            gradient = -2 * inputs[i] * error
            self.weights[i] -= learning_rate * gradient

        # Update bias
        gradient_bias = -2 * error
        self.bias -= learning_rate * gradient_bias