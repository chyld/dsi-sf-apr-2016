#Chapter 7: Hypothesis Testing

##Introduction
Now we have covered the concept of population and sample in ```Chapter 6```, we move on to use hypothesis testing to test assumptions about population parameters based on a sample from the population.

Read [**this page**](http://stattrek.com/hypothesis-test/hypothesis-testing.aspx?tutorial=ap) to make sure you understand the basics of hypothesis testing. The assignment will contain questions where answers can be found in the page.

Then we are going to move onto one of the most common test in hypothesis
testing **t-test**.  **T-tests** is used for samples of **continuous data** (e.g. height as oppose to color). Read the following to get up to speed as to how the different variants of the test is performed.
- [**One sample t-test**](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/one-sample-t-test): Test if a population mean is equal to the a hypothesized value

- [**Two sample unpaired t-test**](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/two-sample-t-test-for-comparing-two-means): Test if 2 populations have the same mean value

- [**Two sample paired t-test**](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/paired-difference-t-test): Test if 2 populations have the same mean value when
there is a one-to-one mapping between the 2 populations, i.e. blood pressure before
treatment and after treatment

##Assignment

- PART 1:  
Answer the questions in ```hypothesis_testing_assignment.md```.

- PART 2:
Follow the below instructions to fill in ```t_test.py```. Any answers that
is not code, please put it as a comment with a ```#``` at the beginning of the
line

- PART 2.1:  
Run ```python t_test.py```, you should see the first 5 values from each
    of the 2 samples

- PART 2.2:
Using the equation given in the reading above, open `t_test.py` and fill in the function ```one_sample_ttest()``` to output the t-statists and p-value of sample data as a tuple. You may use numpy functions which will make your life easier.   e.g. ```np.mean()``` ```np.var()```.


- PART 2.3:
Use the scipy library's built-in function ```scs.ttest_1samp()``` to see if you have implemented ```one_sample_ttest()``` correctly.  Print the output the scipy function results and your function results in your `t_test.py` in the area indicated in the file.

- PART 2.4:  
    If I told you ```sample_1``` is the hours people have worked daily before we brought in a new blend of coffee, and ```sample_2``` is after the new coffee, use the correct function to tell if we should get the new coffee. Include in your answer of how sure you are of your conclusion

- PART 2.5:  
If I told you ```sample_1``` is the hours people have worked daily at company A and ```sample_2``` is hours for people at company B, use the correct function to determine if company A or company B is more productive. Include in your answer of how sure you are of your conclusion


# Resources
- All the statistical test docs for scipy can be found [**here**](http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html)

- For more statistical numpy functions, see [**this**](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)

- The unpaired two sample t-test function is ```scs.ttest_ind()```.
- The paired two sample t-test function is ```scs.ttest_rel()```

- If you'd like, feel free to use ```statistic.py``` from ```Chapter 6```.  Put ```statistics.py``` in the directory where ```t_test.py``` is, and then, in ```t_test.py``` include the line ```import statistics as st``` at the beginning of the file. Subsequently, you can call functions from ```statistics.py``` (e.g. ```st.get_mean```).
