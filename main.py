# def main():
#     print("Hello from lecture-searching!")

from generators import ordered_sequence
from searching import linear_search, binary_search

import time

seq = ordered_sequence(50)
print(seq)

start = time.perf_counter()
resl = linear_search(seq,4)
end = time.perf_counter()

res_2 = linear_search(seq,4)

import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

sizes2 = [200, 400, 5000]
times2 = [0.00001, 0.00003, 0.00006]

plt.plot(sizes, times)
plt.plot(sizes2, times2)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()




