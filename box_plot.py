from matplotlib import pyplot as plt
import seaborn as sns

from import_data import getDataSet

def make_plot():
    data = getDataSet()
    sns.catplot(data=data, x='Obesity', y='Weight', hue='Gender', kind="box")
    plt.title('Weight vs Obesity class')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout(pad=3)

def show_plot():
    make_plot()
    plt.show()
    plt.close()


def save_plot_as(filename):
    make_plot()
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    show_plot()
    save_plot_as('box_plot.png')
