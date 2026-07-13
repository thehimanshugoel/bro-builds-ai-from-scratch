import random 

class Neuron:
    def __init__(self):
        # The computer starts with random guesses
        self.weight = random.uniform(-1,1)
        self.bias = random.uniform(-1,1)  

    
    def predict(self,x ):
        return self.weight * x + self.bias