import wave
import numpy as np


audio_file = "ASax-E4.wav"
sample_rate = 44100

def preprocess_wav(filepath):
    with wave.open(filepath, 'rb') as wavefile:
        # Get the number of frames (samples) in the wave file
        num_frames = wavefile.getnframes()
        # Read the wave file data as a sequence of bytes
        wave_data = wavefile.readframes(num_frames)
        # Convert the byte sequence to a NumPy array of signed 16-bit integers representing the audio signal
        audio_data = np.frombuffer(wave_data, dtype=np.int16)
        
        return audio_data

# Preprocess the wave file and get the scaled audio data
scaled_audio_data = preprocess_wav(audio_file)

# Compute the FFT of the audio data using NumPy
fft_result = np.fft.fft(scaled_audio_data)

# Compute the magnitude of the FFT output
mag = np.abs(fft_result)

# Get the frequency resolution
freq_res = sample_rate / len(mag)

# Create an array of frequencies
freqs = np.arange(0, len(mag)) * freq_res

# Define the cutoff frequency in Hz
cutoff_freq = 600

# Calculate the cutoff index
cutoff_index = int(round(cutoff_freq / freq_res))

# Set the magnitude of the FFT output to zero for high frequencies (THIS IS THE FILTERING ACTION)
fft_result[cutoff_index:len(mag)] = 0

# Take the inverse FFT of the modified complex audio data
filtered_complex_audio_data = np.fft.ifft(fft_result)

# Convert the filtered complex audio data to a list of real numbers
filtered_audio_data = np.real(filtered_complex_audio_data).astype(np.int16)

# Create a new wav file with the filtered audio data
with wave.open("filtered_audio.wav", "wb") as wav_file:
    wav_file.setparams((1, 2, sample_rate, len(filtered_audio_data), "NONE", "not compressed"))
    wav_file.writeframes(filtered_audio_data.tobytes())
