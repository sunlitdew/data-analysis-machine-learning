from import_data import getDataSet
import matplotlib.pyplot as plt
import seaborn as sns

def make_plot():
    data = getDataSet()

    sns.displot(y='Transport', data=data, hue = 'Gender')
    plt.title('Chosen mode of transport by gender')
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