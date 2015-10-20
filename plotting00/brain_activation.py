from nilearn import datasets
import matplotlib.pyplot as plt
from nilearn import plotting

def plot_activation_by_ID(identifier):
    localizer_dataset = datasets.fetch_localizer_contrasts(
            [identifier],
            n_subjects=2,
            get_tmaps=True)
    localizer_tmap_filename = localizer_dataset.tmaps[1]

    plotting.plot_glass_brain(localizer_tmap_filename, threshold=3)

def plot_activation_by_data(localizer_data):
    plotting.plot_glass_brain(localizer_data, threashold=3)
