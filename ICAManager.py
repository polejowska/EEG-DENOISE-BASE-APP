from mne.preprocessing import ICA


class ICAManager(object):
    """ICAManager - class for specifying ICA settings.
    """
    def __init__(self, signal, n_components, method):
        self.signal = signal
        self.n_components = n_components
        self.method = method

    def extract_components(self):
        random_state = 50
        self.ica = ICA(n_components=self.n_components, method=self.method,
                        random_state=random_state)
                    
    def plot_ica_components(self):
        self.extract_components()
        # self.ica.plot_components(layout=self.layout)

    def exclude_ica_components(self, components_to_exclude):
        self.extract_components()
        self.ica.appy(self.raw, exclude=components_to_exclude)