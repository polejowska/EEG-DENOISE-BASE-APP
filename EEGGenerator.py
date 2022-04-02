import numpy as np
import random
import matplotlib.pyplot as plt


class EEGGenerator(object):
    """EEG Generator - class for generating the EEG signal"""

    def __init__(self, fs, start_time, end_time):
        """Initializes EEG signal generator.

        Args:
            fs (int): The number of samples per seconds.
            start_time (int): The starting point time of signal in the time domain.
            end_time (int): The ending point time of signal in the time domain.
        """
        self.fs = fs
        self.start_time = start_time
        self.end_time = end_time
        self.n_samples = fs * end_time
        self.eeg_signal =  np.linspace(self.start_time, self.end_time, self.n_samples)

    def create_signal(self, start_time, end_time, fs, 
                    low_peak_amplitude_value, high_peak_amplitude_value,
                    low_frequency, high_frequency):
        """Creates signal that can be included in the entire EEG signal.

        Args:
            start_time (int): The starting point time of signal in the time domain.
            end_time (int): The ending point time of signal in the time domain.
            fs (int): The number of samples per seconds.
            low_peak_amplitude_value (int): The lowest amplitude point of the signal.
            high_peak_amplitude_value (int): The highest amplitude point of the signal.
            low_frequency (float): The lowest rate of freqency.
            high_frequency (float): The highest rate of frequency.

        Returns:
            np.array: The generated signal.
        """
        n_samples = end_time * fs
        t = np.linspace(start_time, end_time, n_samples)
        signal_amplitude = [round(
            random.uniform(low_peak_amplitude_value, high_peak_amplitude_value), 2)
            for i in range(len(t))
            ]
        signal_frequency = [random.uniform(low_frequency, high_frequency) for i in range(len(t))]
        signal = signal_amplitude * np.sin(2*np.pi*np.asarray(signal_frequency)*t)
        return signal

    def simulate_eeg(self, fs=256, start_time=0, end_time=10):
        """Simulate eeg signal.

        Args:
            fs (int, optional): The sampling frequency. Defaults to 256.
            start_time (int, optional): The start time of the signal. Defaults to 0.
            end_time (int, optional): The end time of the signal. Defaults to 10.

        Returns:
           np.array: The syntethic EEG signal.
        """
        low_peak_amplitude_value = -10
        high_peak_amplitude_value = 10

        gamma_waves = self.create_signal(start_time=self.start_time, end_time=self.end_time, fs=self.fs, 
            low_peak_amplitude_value=low_peak_amplitude_value,
            high_peak_amplitude_value=high_peak_amplitude_value,
            low_frequency=30.0, high_frequency=140.0)
        beta_waves = self.create_signal(start_time=self.start_time, end_time=self.end_time, fs=self.fs, 
            low_peak_amplitude_value=low_peak_amplitude_value,
            high_peak_amplitude_value=high_peak_amplitude_value,
            low_frequency=13.0, high_frequency=30.0)
        alpha_waves = self.create_signal(start_time=self.start_time, end_time=self.end_time, fs=self.fs, 
                    low_peak_amplitude_value=low_peak_amplitude_value,
                    high_peak_amplitude_value=high_peak_amplitude_value,
                    low_frequency=8.0, high_frequency=13.0)
        theta_waves = self.create_signal(start_time=self.start_time, end_time=self.end_time, fs=self.fs, 
            low_peak_amplitude_value=low_peak_amplitude_value,
            high_peak_amplitude_value=high_peak_amplitude_value,
            low_frequency=4.0, high_frequency=8.0)
        delta_waves = self.create_signal(start_time=self.start_time, end_time=self.end_time, fs=self.fs, 
            low_peak_amplitude_value=low_peak_amplitude_value,
            high_peak_amplitude_value=high_peak_amplitude_value,
            low_frequency=0.5, high_frequency=4.0)
        
        # combine all waves into one eeg signal
        eeg_signal = alpha_waves + beta_waves + theta_waves + delta_waves + gamma_waves

        self.signal = eeg_signal

        return eeg_signal

    def visualize(self, signal):
        """Plot the signal.
        """
        plt.title("Generated EEG signal") 
        plt.xlabel("Time") 
        plt.ylabel("Amplitude") 
        plt.plot(signal)
        plt.savefig('static/signal.png')