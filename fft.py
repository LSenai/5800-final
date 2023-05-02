"""
Computes the Discrete Fourier Transform (DFT) of a polynomial P using the 
Fast Fourier Transform (FFT) algorithm.
"""

import cmath

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

