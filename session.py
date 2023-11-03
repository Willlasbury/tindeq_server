from tindeq import TindeqHandler
import numpy as np

class Session:

    def __init__(self):
        self.weights = [] 
        self.tare = 0.0

    def log_force_sample(self, time, weight):
        self.weights.append(weight)

    def mean(self):
        return np.mean(self.weights)