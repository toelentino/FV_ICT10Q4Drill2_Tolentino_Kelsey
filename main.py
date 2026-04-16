from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    document.getElementById('output').innerHTML = " " 

    cases = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    solved_cases = np.array([5, 4, 6, 3, 7, 2, 1])

    plt.plot(cases, solved_cases)

    plt.title("Cases Solved")
    plt.xlabel("Days")
    plt.ylabel("Number of Cases ")

    plt.show()
