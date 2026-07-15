import random


class Neuron:

    def __init__(self):

        # One weight for each input
        self.weights = [
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ]

        self.bias = random.uniform(-1, 1)

    def predict(self, inputs):

        prediction = self.bias

        for x, w in zip(inputs, self.weights):
            prediction += x * w

        return prediction