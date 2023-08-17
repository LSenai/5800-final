# Research Paper - Fast Fourier Transform
Name: Leo Senai

Semester: Spring 2023

Topic: Fast Fourier Transform (FFT)

Link The Repository: [https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-LSenai](https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-LSenai) 


![FFT in a nutshell](/resources/fft_simple.webp)


## Introduction

The algorithm I decided to explore is Fast Fourier Tranform (FFT). I learned about it from a YouTube video titled [7 Algorithms That Rule the World](https://www.youtube.com/watch?v=DsXtYx7RfqE). I wanted to challenge myself with exploring something that filled the following criteria:

* Mathematical depth. I am not a "math person", so I wanted to see if I could learn about and appreciate an algorithm that is relatively complex compared to anything I am familiar with. I thought it may be a good way to prepare for the 5800 course. My goal was to understand the fundamentals of the algorithm, including the underlying mathematics.  
* Personal interest. I am a novice musician and producer, so I thought I would enjoy this assignment if I could relate it to something I find interesting. The result worked, as I ended up spending quite a bit of time learning how to apply this algorithm to audio files, and then filtering the audio as a side project/addition to this assignment. This paper will include side notes about this for the reader if you are interested. I took this as an opportunity for some more inquiry-based learning. 

After watching the video and consuming other content about FFT, I found its applications in music, signals intelligence, wireless connectivity all very interesting and exciting. For this assignment, I focused on a specific implementation of the algorithm known as the Cooley-Tukey FFT algorithm, however it should be noted that there are many other implementations. I chose Cooley-Tukey as it was the foundational algorithm for the development of FFT in computer science. 

### What problem does it solve?
The Fast Fourier Transform algorithm provides an efficient way to calculate the Discrete Fourier Transform (DFT), which essentially means a way to convert a signal from its time domain into its frequency domain (and vice versa). In more mathematical terms, I understood it essentially as a faster way to take a continous signal (such as an sound wave) and break it into discrete individual frequencies. 

![Fourier Transform helps convert signal from time to frequency domain. A signal may be composed of multiple dominating frequencies](/resources/3d%20fft.png)


One example of its application that helped me understand FFT is how it can more efficiently calculate **polynomial multiplication**. The standard way we learned to multiply polynomials is using the distributive property, such as in the example below where we multiply A(x) * B(x):

Let $A(x) = x^2 + 3x + 2$ and $B(x) = 2x^2 + 1$. Using the distributive property, we would have to multiply each term in A by all terms in B, which is a time complexity of $O(n^2)$. However, using FFT, such computations can be completed in $O(n logn)$ time, which is significantly faster. The same comparison holds for the traditional discrete Fourier Tranform, which operates at $O(n^2)$ [^1].

In addition to the above large polynomial computation example, these algorithms have a range of applications in spectometry, digital recording, modulation of data (for example in 5G, WiFi, etc.), so in many ways, it  can be found in use everywhere. 

The history of the FFT algorithm itself is also interesting. While the original idea goes back to Carl Gauss, the modern algorithm is known to be credited to James Cooley and John Tukey. According to Wikipedia, *"Tukey came up with the idea during a meeting of President Kennedy's Science Advisory Committee where a discussion topic involved detecting nuclear tests by the Soviet Union by setting up sensors to surround the country from outside. To analyze the output of these sensors, an FFT algorithm would be needed. In discussion with Tukey, Richard Garwin recognized the general applicability of the algorithm not just to national security problems, but also to a wide range of problems..."* [^2]. Fortunately, due to the fact that Tukey did not work at IBM, the algorithm was not patented and instead went in to the public domain. This meant that anyone was free to use it, and I think it is safe to say that the algorithm was critical to the development of many revolutionary digital technologies. 

### Paper Outline:

This paper will continue with a general analysis of the FFT algorithm, followed by a brief discussion of my impleemtnation of FFT (and DFT for comparison). We will then conduct some emperical analysis that compares my implementation of the Cooley-Tukey FFT vs a naive Discrete Fourier Transformation. We will then compare my FFT against the FFT in the Python NumPy library, which is considerably faster. Finally there will be a deeper demonstration of the applications of FFT as well as a brief recap of its applications. We will end with a summary of observations and reflections. 

## Analysis of Algorithm

As mentioned above, the FFT algorithm has a time complexity of $O(n logn)$ and it is a way of computing the Discrete Fourier Transform (DFT). DFT transforms a sequence of N complex numbers ${x_n} := x_0, x_1,..., x_{N-1}$ into another sequence of complex numbers, ${X_k} := X_0, X_1,..., X_{N-1}$, which is defined by $X_k = ∑_{n=0}^{N-1} x_n e^{-\frac{2\pi i}{N}kn}$. 

The basic idea behind FFT is to divide the DFT calculation into smaller sub-problems, and then recursively solve these sub-problems using smaller DFTs. This is known as the "divide-and-conquer" approach.

The key to achieving the $O(n log n)$ time complexity is the fact that the DFT has a symmetry property that allows the sub-problems to be computed efficiently. Specifically, the DFT of a sequence of length n can be written as the sum of two DFTs of sequences of length $n/2$, plus some additional calculations that can be performed in $O(n)$ time. This relationship is known as the "butterfly" equation.

Using this equation, we can compute the DFT of a sequence of length n by recursively computing the DFTs of two sequences of length $n/2$, and then combining the results using the butterfly equation. This process can be repeated until we reach sequences of length 1, which can be computed in constant time.

Each level of recursion involves computing $O(n)$ operations (to calculate the additional terms in the butterfly equation), and there are $log n$ levels of recursion (since we are dividing the sequence in half at each level). Therefore, the total number of operations required to compute the DFT using FFT is $O(n log n)$.

In summary, the FFT algorithm achieves its O(n log n) time complexity by exploiting the symmetry properties of the DFT, and recursively dividing the computation into smaller sub-problems that can be solved efficiently.

The space complexity can vary slightly based on implementation, but is generally considered to be $O(n)$, where $n$ is the length of the input polynomial. 

## Implementation

I chose to implement the FFT algorithm in Python, due to its ease of use and the variety of available libraries one can employ. While the NumPy library has its own implementation of the FFT, I implemented my own take of the basic Cooley-Tukey algorithm, which only works with values of $N$ that are powers of two. 
When the input size is a power of 2, the algorithm can be applied recursively until the base case of DFTs of size 2 is reached, at which point the DFT can be computed using only additions and subtractions.

When the input size is not a power of 2, the Cooley-Tukey algorithm can still be applied, but it requires additional computation to break down the input sequence into smaller DFTs of size 2 or 4. This additional computation can result in a slower algorithm and a larger constant factor in the time complexity. There are other implementations of FFT that allow for any size n, however I chose Cooley-Tukey as it is considered the "standard" or baseline for understanding FFT, and others may be more complex.


[My implementation](/fft.py) of the algorithm is based on the pseudocode provided in [this lengthy explainer video](https://www.youtube.com/watch?v=h7apO7q16V0 ) of the FFT. While the mathematical concepts underpinning the algorithm are beyond my complete grasp, the pseudocode (and video) made it relatively easy to understand how to implement the algorithm in python. Here is the pseudocode from the video:

![](/resources/FFT_pseudocode_screenshot.png)

And below is my implementation, which uses the cmath library:


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


The biggest challenge for this implementation was figuring out how to represent omega, which represents the roots of unity in the algorithm and are central to making it work. These are complex numbers that satisfy the equation $\omega^n = 1$, where n is the length of the input sequence. Frankly, I still do not have a good grasp on the concepts of roots of unity, but understand that this is the driving force in factoring the DFT into smaller bits and employing a divide and conquer method. Below is a review/summary of the code:

- The FFT function takes a list P as input, where P represents a coefficient representation of a polynomial. 
- The n variable stores the length of the input list P. If the length is 1, the function returns P since the DFT of a single element is the element itself.

-   The omega variable is initialized as the complex exponential function, which is used to compute the roots of unity. The roots of unity are used in the FFT algorithm to factorize the DFT computation and improve the time complexity.

- The input list P is split into two parts, Peven and Podd, which represent the even and odd-degree terms of the polynomial.

* The fft function makes recursive calls to itself to compute the DFT of the even-degree terms and the odd-degree terms.

- The final DFT of the input list P is computed by combining the DFTs of the even and odd-degree terms using the butterfly operation. The y variable is used to store the output list, which represents the final DFT.

- The for loop iterates over the range of n/2 and calculates the values of y[j] and y[j + n/2] using the computed values of Yeven and Yodd, and the precomputed value of omega ** j. The butterfly operation combines the values of Yeven and Yodd using the roots of unity to calculate the final DFT coefficients.

- The function returns the list y, which represents the DFT of the input list P.

### Side Note:

To give myself an additional challenge and to relate this algorithm to a personal interest, I wanted to see if I could use the algorithm on an audio file. I think wanted to see if I could use a finding from this algorithm to filter the audio. Though a bit beyond the scope of this assignment, it was a positive learning experience and came with the added challenge of figuring out how to process audio data so that it could be input into my implementation. This ultimately gave me a better understanding of my implementation, how it might be used, and its potential limitations. I provide some additional discussion/context around this at the end of this paper. 

## Empirical Analysis

For my emperical analysis, I looked into two relatively straightforward comparisons. Firstly, I wanted to demonstrate the relative speed of FFT vs DFT. As a reminder, FFT is $O(nlogn)$ while the naive DFT is $O(n^2)$. I [wrote a python file](/fft_vs_dft.py) that compares my FFT implementation against a DFT function. The user can use this to compare runtime of the two functions. One limitation is that there may be some variation in the output due to the use of complex numbers, so it was hard to evaluate the output of the two functions as equal, however when running it on a small size n, one can observe that they achieve similarly close outputs. Also note that the size of n must equal a power of 2. 

It is obvious that given the differences in Big-O, FFT will perform much faster. My implementation yielded the following results of runtime (in seconds):

| values of n | DFT         | FFT            |
|-------------|-------------|----------------|
| 2048        | 2.747523546 | 0.00997543335   |
| 1024        | 0.816163063 | 0.003990650177  |
| 512         | 0.2309064865| 0.001994848251  |
| 256         | 0.0393974781| 0.0009615421295 |
| 128         | 0.008976221085| 0              |

![](/resources/runtime_comparison.png)

I wrote [this script](/comparison.py) to generate the chart above, which anyone is welcome to try. You can observe that FFT rightfully earns its name as the *fast* fourier transform. 

However it was interesting to see how much faster it could be. Knowing that the NumPy library has its own implementation, I also [compared](/precision_comparison.py) the speeds of these two. In this implementation, I even used high precision complex number values for my implementation, which comes with some additiona overhead, but will make it more comparable to the NumPy version. It was a bit shocking to see how much faster the NumPy implementation is: 

![](/resources/runtime_comparisons_FFTs.png)

Here is another view using two y-axes to compare respective runtimes:
![](/resources/twin%20axes%20comparison.png)

The NumPy implementation is faster likely due to several reasons such as using parallelization, optimizied memory allocation, and other forms of optimization. 

### FFT and Music: 
I took this opportunity to try and use my FFT implementation on an audio file. I wanted to get "hands on" with this assignment. I decided to use an 8 second clip of saxophone audio from an [open source sound library](https://zenodo.org/record/3685367) used for audio research. This library has a large dataset of isolated music notes from various orchesta instruments. I chose alto sax, as a tribute to my brother who is learning saxophone. 

Digital audio is relevant to this assignment because it represents a way in which sound signals are captured and processed using discrete samples that capture the waveform of sound. A sound wave has three main properties:

1. Amplitude: the magnitude of the wave signal, usually measured in decibels.
2. Time: the duration of the wave.
3. Frequency: "represents how many complete cycle the wave takes in one second and it is measured in Hz." 

![](/resources/signals3D_4.png)

[source](https://medium.com/analytics-vidhya/audio-data-processing-feature-extraction-science-concepts-behind-them-be97fbd587d8)

It may help to think about it like video -- video is compiled using several individual frames/pictures per second. Digital audio works the same way -- all digital audio has a certain amount of "sound bits" per second, which is known as sample rate. Most professional media uses a sample rate of 44,100 audio samples per second (or 44.1 kHz). Interestingly, although humans can only hear roughly up to the range of 20 kHz, it is theorized that the sample rate of audio must be at least twice that in order to reconstruct it [^3].

This becomes an appropriate opportunity to use FFT because of the large size of data present in an audio file, which digitally represents/recreates sound waves. In this case, I am using FFT to transform time-domain signals (such as an audio wavform file) into the frequency domain. 

In other words, I use FFT convert a digital sound wave file ([source code](/soundwave.py)):

![](/resources/alto%20sound%20looks%20like%20this.png)

and get the sound's frequencies:
![](/resources/alto%20sounds%20like%20this.png)

Note above that I labeled 'Amplitude' and 'Magnitude 'interchangableby. 

In the 8 second clip, which has a sample rate of 44.1kHz, the data 355,645 elements in it. After zero-padding the data (meaning bringing it up to a usable power of 2), the array had a size of 524,288. 

With an N value of that size, the naive DFT algorithm is simply not feasible -- it would take decades! However, using this [script](/fft_on_audio.py), you can see that the FFT implementation took just a few seconds:
![](/resources/audio_FFT_demo.png)

As a final demonstration of what you might be able to do with this, I wrote a script that allows you to filter out sounds above a certain frequency. This is my novice attempt at creating a low pass filter - which is common in audio/music editing. A low pass filter filters out all frequencies above a certain cutoff range. A real filter would be much more sophisticated, however this was a useful way to explore the topic of FFT. You can listen to the filtered saxophone [here](/filtered_audio.wav), or play with the code [here](/low_pass_filter.py). For this implementation, I entirely used the numpy library and abandoned my implementation as it functioned better. One can see how such an approach can be used for things such as audio editing and noise cancellation.

## Application

I hope that the above exploration of FFT and audio demonstrated some of its uses. While elementary, the algorithm is used for a range of very sophisticated applications relataed to signals, such as WiFi and 5G, and medical imaging. I imagine it is used for things such as noise cancellation, or even powering popular applications like Shazam.[^4]

As demonstrated, FFT is useful for being able to process signals at speeds that make a lot of digital technology possible. Without its $O(nlogn)$ run time, it is likely that technologies such as WiFi would not be possible. 


## Summary

Having known nothing about the Fast Fourier Transform (or Discrete for that matter), and despite no formal training in linear algebra and calculus, I can still understand and appreciate the profound utility and elegance of the FFT algorithm and its importance to so many applications in digital technology. Applying the algorithm to an audio file helped me better understand how it might be used. It was also interesting to learn about how polynomials can be expressed in a 1-D matrix through the coeffecient representation, and how this basic type of data structure enables a very complex algorithm. 

I hope that in my free time I now grow the confidence to play with other algorithms that allow me to process and use signals for interesting, socially meaningful, or creative applications. 


## Footnotes and Sources

[^1]: YouTube. (2020, November 14). The fast fourier transform (FFT): Most ingenious algorithm ever? YouTube. Retrieved April 21, 2023, from https://www.youtube.com/watch?v=h7apO7q16V0 

[^2]: Wikimedia Foundation. (2023, March 24). Fast fourier transform. Wikipedia. Retrieved April 21, 2023, from https://en.wikipedia.org/wiki/Fast_Fourier_transform#Applications 

[^3]: Velayadham, V. (2020, May 2). Audio Data Processing- Feature Extraction - science &amp; concepts behind them. Medium. Retrieved April 21, 2023, from https://medium.com/analytics-vidhya/audio-data-processing-feature-extraction-science-concepts-behind-them-be97fbd587d8 

[^4]: 
* O’Sullivan, J. How we made the wireless network. Nat Electron 1, 147 (2018). https://doi.org/10.1038/s41928-018-0027-y
* Fourier transform (ft). Questions and Answers ​in MRI. (n.d.). Retrieved April 22, 2023, from https://mriquestions.com/fourier-transform-ft 
* additional sources around applications are linked above and below

#### Additional Sources used:
* An introduction to the discrete fourier transform - technical articles. All About Circuits. (n.d.). Retrieved April 21, 2023, from https://www.allaboutcircuits.com/technical-articles/an-introduction-to-the-discrete-fourier-transform/ 
* VanderPlas, J. (n.d.). Understanding the FFT algorithm. Understanding the FFT Algorithm | Pythonic Perambulations. Retrieved April 21, 2023, from https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/ 

* Wikimedia Foundation. (2022, December 19). Butterfly diagram. Wikipedia. Retrieved April 21, 2023, from https://en.wikipedia.org/wiki/Butterfly_diagram

* https://numpy.org/doc/stable/reference/routines.fft.html 
* https://zenodo.org/record/3685367
