import numpy as np
import matplotlib.pyplot as plt


def get_coordinate(num):
    return num * np.cos(num), num * np.sin(num)


def create_plot(nums, figsize=8, s=None, show_annot=False):
    plt.style.use("dark_background")
    nums = np.array(list(nums))
    x, y = get_coordinate(nums)

    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.scatter(x, y, s=s)
    for num in nums:
        ax.annotate(num, (x[num], y[num]))
    plt.axis("on")
    plt.show()
