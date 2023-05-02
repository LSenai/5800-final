"""
Computes the Discrete Fourier Transform (DFT) of a polynomial P using the 
Fast Fourier Transform (FFT) algorithm.
"""

import time
from fft import fft
from preprocess_wav import preprocess_wav

audio_file = "ASax-E4.wav"


# Preprocess the wave file and get the scaled audio data
scaled_audio_data = preprocess_wav(audio_file)

# Convert the scaled audio data to a list of complex numbers
complex_audio_data = [complex(x, 0) for x in scaled_audio_data]

# Measure the time it takes to compute the DFT of the polynomial using the fft function
start_time = time.time()
DFT = fft(complex_audio_data)
end_time = time.time()

# Compute the runtime of the fft function
runtime = end_time - start_time

print("Runtime:", runtime, "seconds")
