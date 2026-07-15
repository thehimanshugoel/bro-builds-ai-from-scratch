import random


class Neuron:

    def __init__(self):
        self.weight = random.uniform(-1, 1)
        self.bias = random.uniform(-1, 1)

    def predict(self, x):
        return self.weight * x + self.bias

    def learn(self, x, actual, prediction, learning_rate=0.01):

        # Gradient of loss with respect to weight
        gradient_weight = -2 * x * (actual - prediction)

        # Gradient of loss with respect to bias
        gradient_bias = -2 * (actual - prediction)

        # Gradient Descent update
        self.weight -= learning_rate * gradient_weight
        self.bias -= learning_rate * gradient_bias