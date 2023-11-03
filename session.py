import numpy as np

class Session:
    
    def __init__(self):
        self.weights = []
        self.tare = 0.0

    def log_force_sample(self, time, weight):
        self.weights.append(weight)
        return self.weights

    def mean(self):
        if len(self.weights) != 0:
            value = np.mean(self.weights)
            return value 
        else:
            return ValueError('no data in weights')
            

    
    def clear(self):
        self.weights = []