#Chapter 6: Frequentist Statistics

##Introduction
We are going to implement functions to calculate some basic statistics here.
The main goal is to jostle your memory on these statistics, and at the same
time gently introduce you to more of the scipy and numpy functionalities.

##Assignment
Follow the below instructions to fill in ```statistics.py```. If you are
stuck at any point, refer to ```statistics_review.md```.

- Scroll to the bottom of the ```statistics.py```, you will see
```if __name__ == '__main__':```. The code below that will be executed when you
run in your command prompt ```python statistics.py```

- You will be implementing all the functions at the beginning of the script
and will be calling the functions at the bottom after
 ```if __name__ == '__main__':```, e.g.

```
if __name__ == '__main__':
    population = load_pickle('arr.pkl')
    print 'First 5 element of the population: ', population[:5]
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)
    population_mean = get_mean(population)
    sample_100_mean = get_mean(sample)
    sample_1000_mean = get_mean(sample)
    print 'Population mean: ', population_mean
    print 'Sample 100 mean: ', sample_100_mean
    print 'Sample 1000 mean: ', sample_1000_mean
    ...
```

- Go ahead and run the script (```python statistics.py```) and you will see
5 numbers printed out. These are the first 5 elements in the population list
I have provided you with. ```population``` is a numpy array

**Before we start, this exercise is meant for you to implement the equations
yourself, you should not use the numpy functions ```np.mean()```,
```np.sem()``` and ```np.var()``` here.
Feel free to use any other numpy /scipy functions as you see fit.**

**Also if there is a question asked that does not involve code, please answer
by putting a comment in by using the hash ```#```. Put the answers after
```if __name__ == '__main__':```**


- Implement ```draw_sample()``` to draw a number of members randomly from the
population.

    - Define a ```sample_100``` variable which draws 100 members at the bottom.

    - Define a ```sample_1000``` variable which draws 1000 members at the bottom.

- Implement ```get_mean()``` to find the mean given an array of numbers.
Call ```get_mean()``` at the bottom to calculate population mean and
sample mean. Print the mean values

- Implement ```get_variance()``` to find the sample variance and population
variance. See ```statistics_review.md``` to see the difference between the
two variances. You will need to have the function take in a ```sample```
parameter which if set to ```True```, will calculate sample variance, otherwise
population variance. Call the function to find both sample and population
variances. Print them out. You should have a population variance, sample 100
variance and sample 1000 variance.

    - What is the percentage difference between variance of the sample
    of 1000 and variance of the sample of 100?

- Implement ```get_sem()``` to calculate the standard error of the sample
mean. The standard error of the mean measures how precisely we know the
true mean of the population. Define and calculate the variables
```sem_100``` and ```sem_1000``` by applying ```get_sem()``` to the 100
sample and 1000 sample. Print the values.

    - What is the percentage difference between SEM of the sample
    of 1000 and SEM of the sample of 100?
    - What information the SEM tells us that the variance does not?

- Implement ```get_confidence_interval()``` to calculate the confidence
intervals of the 100 sample and 1000 sample using confidence of ```.95```
Define the variables ```ci_100``` and ```ci_1000``` and apply the function.
Print the variables. You might want to vist ```statistics_review.md``` at this
point for the equation.

    - **Hint 1**: Use ```get_mean()``` and ```get_sem()``` defined above.

    - **Hint 2**: Use ```scs.t.ppf(percentile)``` to get a value at a given
    percentile in a t-distribution

    - Does the confidence intervals include the population mean? Can you explain
    why that is?

    - Try lowering the confidence to **.7** instead of **.95**, what does it
    do to the range of the confidence interval?
    Can you explain why that is?

    - **Extra**: What assumption are we making about the distribution of the
    population when we apply the confidence interval? Why are we able to make
    this assumption here without visualizing the plot?

- Implement ```get_interquartile_range()``` to calculate the range of
the mid-50 percent of the population. Use ```np.percentile(n)``` to get the
nth percentile of the data

    - We will use the function in ```get_outlier()``` below

- Implement ```get_outlier()``` by using ```get_interquartile_range()```.
Any data points 3 interquartile range below Q1 (25th percentile) or
3 interquartile range above Q3 (75th percentile) are considered to be
outliers.

    - Find and print out the outliers in the distribtion as a list

