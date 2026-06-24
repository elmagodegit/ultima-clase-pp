import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.arange(100)
    y = np.random.normal(size=100)

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    fig.savefig("plot.png")


if __name__ == "__main__":
    main()
