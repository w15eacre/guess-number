# Project 0. Guess the Number

## Table of Contents  
[1. Project Description](#project-description)  
[2. What Problem Are We Solving?](#what-problem-are-we-solving)  
[3. Brief Information About the Data](#brief-information-about-the-data)  
[4. Results](#results)  
[5. Conclusions](#conclusions)  

### Project Description    
Guess the number chosen by the computer with the minimum number of attempts.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### What Problem Are We Solving?    
The task is to write a program that guesses the number with the minimum number of attempts.

**Competition Conditions:**  
- The computer selects an integer between 0 and 100, and we need to guess it. By "guess," we mean "write a program that guesses the number."
- The algorithm considers whether the random number is greater or less than the target number.

**Quality Metric**     
Results are evaluated by the average number of attempts over 1000 repetitions.

**What We Practice**     
We learn to write good Python code.

### Brief Information About the Data
The input data is a number in the half-open interval [1, 101).

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  
The binary search algorithm is several orders of magnitude more efficient than random guessing. The complexity of such an algorithm is $O(\log(N))$.

Random guessing does not guarantee that the answer will be found in a reasonable number of attempts. However, due to uniform distribution, the correct number will be found on average in about 100 attempts, since the distribution is uniform. The complexity of such an algorithm is Amort. $O(N)$. Moreover, simple brute-force of all values provides greater efficiency $O(N)$.

In the general case, when the probability of each number appearing is equal $p(\omega) = \frac{1}{N}$, where $|\Omega(\omega)| = N$, the probability that the number will not appear is $q(\omega) = 1 - p(\omega)$. Thus, the number will be found with 99% probability if $N = 100$.

$p(\omega) = 0.01$

$1 - q(\omega)^n \geqslant 0.99 \Rightarrow n \geqslant 466$

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Conclusions  
Using pseudo-random numbers for "guessing" results in a low probability of finding the correct answer on the first attempt. But on average, it takes $O(N)$, which does not differ from the brute-force algorithm.

Binary search provides a stable result of $O(\log(N))$.

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find the information in this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️.
