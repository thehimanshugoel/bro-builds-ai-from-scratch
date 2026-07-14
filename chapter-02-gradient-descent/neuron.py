import random 

class Neuron:
    def __init__(self):
        # The computer starts with random guesses
        self.weight = random.uniform(-1,1)
        self.bias = random.uniform(-1,1)  

    
    def predict(self,x ):
        return self.weight * x + self.bias
    

    def learn(self, x, actual, prediction):
        error = actual - prediction

        self.weight += error * 0.01
        self.bias += error * 0.01