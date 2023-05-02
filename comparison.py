import cmath
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def fft(P):
    n = len(P)
    if n == 1:
        return P
    omega = cmath.exp((2j * cmath.pi) / n)
    Peven, Podd = P[::2], P[1::2]
    Yeven, Yodd = fft(Peven), fft(Podd)
    y = [0] * n
    for j in range(n // 2):
        y[j] = Yeven[j] + (omega ** j) * Yodd[j]
        y[j + n // 2] = Yeven[j] - (omega ** j) * Yodd[j]
    return y

def dft(x):
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-2j * cmath.pi * k * n / N)
    return X

n_values = [128, 256, 512, 1024, 2048, 4096]
dft_runtimes = []
fft_runtimes = []

for n in n_values:
    x = [random.random() for i in range(n)]
    
    start_time = time.time()
    dft_result = dft(x)
    end_time = time.time()
    dft_total_time = end_time - start_time
    dft_runtimes.append(dft_total_time)
    
    start_time = time.time()
    fast_result = fft(x)
    end_time = time.time()
    fft_total_time = end_time - start_time
    fft_runtimes.append(fft_total_time)
  
    
plt.plot(n_values, dft_runtimes, label="DFT")
plt.plot(n_values, fft_runtimes, label="FFT")
plt.xlabel("N")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime comparison of DFT and FFT")
plt.legend()
plt.show()
