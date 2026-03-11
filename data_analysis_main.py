import os

from box_plot import save_plot_as as save_box_plot
from histogram import save_plot_as as save_histogram
from histogram_with_hue import save_plot_as as save_histogram_with_hue
from linreg import save_plot_as as save_linreg
from violin_plot import save_plot_as as save_violin_plot
from correlation_matrix import save_matrix_as as save_correlation_matrix
from pca import save_plot_as as save_pca
from stats import save_csvs

save_csvs()
os.makedirs("plots", exist_ok=True)
save_correlation_matrix("plots/correlation_matrix.png")
save_histogram("plots/histogram.png")
save_histogram_with_hue("plots/histogram_with_hue.png")
save_linreg("plots/linreg.png")
save_violin_plot("plots/violin_plot.png")
save_box_plot("plots/box_plot.png")
save_pca("plots/pca.png")