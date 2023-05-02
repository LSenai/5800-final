"""
Comparison of runtimes for the FFT algorithm vs DFT. 
"""

import cmath
import random
import time
import numpy as np # using to assert the resulting values are equal using the allclose function

"""
Computes the Discrete Fourier Transform (DFT) of a polynomial P using the 
Fast Fourier Transform (FFT) algorithm.
"""
def fft(P):
    n = len(P)
    if n == 1:
        return P
    omega = cmath.exp((2j * cmath.pi) / n)  # define the omega value
    Peven, Podd = P[::2], P[1::2]  # split the polynomial into even and odd-degree terms
    Yeven, Yodd = fft(Peven), fft(Podd)  # recursive calls to compute DFT of even and odd-degree terms
    y = [0] * n  # initialize the output list for final value representation
    for j in range(n // 2):
        y[j] = Yeven[j] + (omega ** j) * Yodd[j]
        y[j + n // 2] = Yeven[j] - (omega ** j) * Yodd[j]
    return y

"""
This is an implementation of the Discrete Fourier Tranform (DFT), which is O(n^2). I am implementing it for comparison
purposes to demonstrate how FFT is faster. 
"""
def dft(x):
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-2j * cmath.pi * k * n / N)
    return X


x = [random.random() for i in range(2048)]

print(f"Size of N is: {len(x)}")

start_time = time.time()
dft_result = dft(x)
end_time = time.time()

total_time = end_time - start_time
print("Total DFT runtime: ", total_time)

start_time = time.time()
fast_result = fft(x)
end_time = time.time()
total_time = end_time - start_time

print("Total FFT runtime: ", total_time)