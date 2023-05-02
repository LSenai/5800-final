import wave
import math

def preprocess_audio(filepath):
    with wave.open(filepath, 'rb') as wavefile:
        # Get the number of frames (samples) in the wave file
        num_frames = wavefile.getnframes()
        # Just a check for framerate
        frame_rate = wavefile.getframerate()
        # Read the wave file data as a sequence of bytes
        wave_data = wavefile.readframes(num_frames)
        # Convert the byte sequence to a list of integers representing the audio signal
        audio_data = list(wave.struct.unpack(f"{num_frames}h", wave_data))
        data_size = len(audio_data)
        
        # Zero-pad the audio data to the nearest power of 2
        padded_size = int(math.pow(2, math.ceil(math.log2(data_size))))
        padded_audio_data = audio_data + [0] * (padded_size - data_size)
        
        print(f"This file has a sample rate of {frame_rate}. Meaning there are this many audio samples per second.")
        print(f"The audio data has {data_size} elements in it")
        print(f"After zero-padding, the audio data has {padded_size} elements in it")

    return padded_audio_data