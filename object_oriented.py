# %%
import numpy as np

# %%
# Un str est un type d'objet.
mot = "allo"

# %%
# L'objet a des méthodes
mot.upper()

# %%
# Un tableau numpy est aussi un type d'objet avec des méthodes
a = np.array([1,2,3,4,5])

# %%
a.max()

# %%
# On peut créer nos propres types d'objet
# Ce n'est pas un très bon exemple. Dataset pourrait être remplacé par un tableau
# pandas ou autre. Mais but est d'avoir un cas simple
class Dataset:
    # La fonction init crée l'objet
    # On doit toujours inclure self comme premier argument
    def __init__(self, x: np.ndarray[float], y: np.ndarray[float], yerr: np.ndarray[float]):
        self.x = np.atleast_1d(x)
        self.y = np.atleast_1d(y)
        self.yerr = np.atleast_1d(yerr)

    def __repr__(self) -> str:
        return f"X: {self.x}\nY: {self.y}\nY error: {self.yerr}\n"

# %%
# On peut en créer un ensuite
data = Dataset(a, a*2, np.ones_like(a))

# %%
data

# %%
# Je peux ajouter des attributs à mon objet (pas une bonne idée)
data.name = "Cooldata"

# %%
# On peut créer une sous-classe
class NormalizedDataset(Dataset):
    def __init__(self, x: np.ndarray[float], y: np.ndarray[float], yerr: np.ndarray[float]):
        # On applique le __init__ du parent
        super(NormalizedDataset, self).__init__(x, y, yerr)

        # On normalise directement
        self._y_orig = self.y.copy()
        self._yerr_orig = self.yerr.copy()

        self.yerr = self.yerr / self.y.mean()
        self.y = self.y / self.y.mean()

# %%
norm_data = NormalizedDataset(a, a*2, np.ones_like(a))

# %%
norm_data
