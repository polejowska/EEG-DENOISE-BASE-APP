from sklearn.decomposition import PCA


class PCAManager(object):
    """PCAManager - class for specifying PCA settings.
    """
    def __init__(self, signal, n_components):
        self.signal = signal
        self.n_components = n_components

    def extract_components(self):
        self.pca = PCA(n_components=self.n_components)
                    
    def plot_pca_components(self):
        self.extract_components()

    def exclude_ica_components(self, components_to_exclude):
        self.extract_components()
        self.pca.appy(self.raw, exclude=components_to_exclude)