from matplotlib import pyplot as plt
import seaborn as sns

from import_data import getDataSet





def make_plot():
    data = getDataSet()
    sns.catplot(data=data, x='Monitoring', y='Obesity', hue='Gender', kind="violin", split=True)
    plt.title('Effect of monitoring calorie intake on obesity')
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