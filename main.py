from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    document.getElementById('output').innerHTML = " " 

    boxes = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_boxes = np.array([4, 2, 3, 4, 7, 3, 1])

    plt.plot(boxes, sold_boxes)

    plt.title("Donuts Sold")
    plt.xlabel("Days")
    plt.ylabel("Number of Boxes")

    plt.show()
