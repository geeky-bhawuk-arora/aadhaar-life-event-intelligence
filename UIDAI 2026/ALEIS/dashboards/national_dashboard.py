import matplotlib.pyplot as plt

def plot_trend(series, title):
    plt.figure()
    series.plot()
    plt.title(title)
    plt.show()
