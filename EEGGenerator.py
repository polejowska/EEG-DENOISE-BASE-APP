import numpy as np


class EEGGenerator(object):
    """EEG Loader - class for generating the EEG signal"""

    def __init__(self, amplitude, n, fs):
        self.amplitude = amplitude
        self.n = n
        self.fs = fs

    def simulate(self):
        t = np.arrange(self.n)


    def visualize(self):
        """Plot the signal.
        """
        pass