import numpy as np
import matplotlib.pyplot as plt
import time
import random

def fft(P):
    n = len(P)
    if n == 1:
        return P
    omega = np.exp((2j * np.pi) / n)
    Peven, Podd = P[::2], P[1::2]
    Yeven, Yodd = fft(Peven), fft(Podd)
    y = np.zeros(n, dtype=np.complex128)
    for j in range(n // 2):
        y[j] = Yeven[j] + (omega ** j) * Yodd[j]
        y[j + n // 2] = Yeven[j] - (omega ** j) * Yodd[j]
    return y


n_values = [1024, 2048, 4096, 8192, 16384]
numpy_runtimes = []
my_fft_runtimes = []

for n in n_values:
    x = [random.random() for i in range(n)]
    
    start_time = time.time()
    numpy_result = np.fft.fft(x)
    end_time = time.time()
    dft_total_time = end_time - start_time
    numpy_runtimes.append(dft_total_time)
    
    start_time = time.time()
    my_fft_result = fft(x)
    end_time = time.time()
    fft_total_time = end_time - start_time
    my_fft_runtimes.append(fft_total_time)

    print(f"Results for n = {n}")
    print(f"DFT result: {numpy_result}")
    print(f"FFT result: {my_fft_result}")
    
    
plt.plot(n_values, numpy_runtimes, label="Numpy FFT")
plt.plot(n_values, my_fft_runtimes, label="My FFT")
plt.xlabel("N")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime comparison of FFT Implementations")
plt.legend()
plt.show()

''' to use different y axis, for better visual comparison: '''
fig, ax1 = plt.subplots()

ax1.plot(n_values, numpy_runtimes, label="Numpy FFT", color='b')
ax1.set_xlabel("N")
ax1.set_ylabel("Numpy FFT runtime (seconds)", color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(n_values, my_fft_runtimes, label="My FFT", color='r')
ax2.set_ylabel("My FFT runtime (seconds)", color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title("Runtime comparison of FFT Implementations")
plt.show()