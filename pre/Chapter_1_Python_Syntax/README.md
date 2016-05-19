# Chapter 1:  Python Best Practices

**Read all instructions below, then fill in the functions provided for you in each file located in the code folder**
Practice makes perfect, therefore our first official Galvanize assignments will be just that.  Practicing python.  In particular we'll be getting more comfortable with Python built-in functions and data structures.

The course will heavily use Python for most of its analyses/projects.  It is not
necessary to be an expert in Python coming into the course (that is what we will
teach you!) but it is helpful to be familiar with its syntax.

Not everyone knows Python (or what parts to focus on in the classroom).  We
have provided resources here to get any student familiar with another
programming language up to speed with Python quickly (both in terms of syntax
and style).

Follow the installation instructions directly below to get setup.  Then continue on to the assignments.  

## Installing

We use the [Anaconda](https://store.continuum.io/cshop/anaconda/) Python 2.7
(not Python 3) distribution and use [conda](http://www.continuum.io/blog/conda)
to install any additional packages. You should install Anaconda now.

## Resources

If you still feel new to Python, you might benefit from looking at one of these resources:
* [Dive Into Python](http://www.diveintopython.net/)
* [Learn Python the Hard Way](http://learnpythonthehardway.org/)
* [Effective Python](http://www.effectivepython.com/)

Here's a couple coursera courses on programming in Python as well:
* [Learn to Program: The Fundamentals](https://www.coursera.org/course/programming1)
* [Learn to Program: Crafting Quality Code](https://www.coursera.org/course/programming2)

Lecture notes:
* [notes](python.md) goes over some more advanced python topics.

Python also has great documentation which is helpful if you need to look up how something is done in Python:
* [Python tutorial](https://docs.python.org/2/tutorial/)
* [Python library](https://docs.python.org/2/library/)

## Assignment

#### 1. Practice with built-ins

Fill in the functions in [1_problems.py](code/1_problems.py).

These are all one-liners that use a bunch of handy built-in functions.

#### 2. Generating text

Fill in the functions `word_counts`, `associated_words` and `make_random_story`
in [2_words.py](code/2_words.py). These will give you practice with reading files, strings and dictionaries.

Take a look at the [Collections module](https://docs.python.org/2/library/collections.html).
You may be able to use `DefaultDict` and `Counter` to simplify your code.

#### 3. Fizz Buzz fun with Python

FizzBuzz is infamous for being a simple programming problem that [a lot of software
engineers struggle with](http://blog.codinghorror.com/why-cant-programmers-program/).

* Implement the function `fizzbuzz` in [3_fizzbuzz.py](code/3_fizzbuzz.py). Don't worry, this is not the main point of this question.

* Modify the function definition so that the following calls all work. You should have 3 and 5 be the default parameters.
([documentation](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values))

        fizzbuzz(15)                  # "FizzBuzz"
        fizzbuzz(15, fizz=4)          # "Buzz"
        fizzbuzz(15, buzz=4)          # "Fizz"
        fizzbuzz(15, fizz=6, buzz=7)  # ""

    Now in the main block you should be able to remove the 2nd and 3rd parameters.

* Look at how the main function uses `sys.argv`. You can run your program with this
command in the command line:

        python 3_fizzbuzz.py 20

    Modify `words.py` so that you can run your program like this:

        python 2_words.py alice.txt 200

    You'll have to import the `sys` module and use `sys.argv` ([documentation](https://docs.python.org/2/library/sys.html))

---
<br>

## What you need to know

##### You should be comfortable with everything below.

* Basic data structures and associated methods
  * int, float
  * string
  * list
  * dict
  * set
  * range
* Control structures
  * if, elif, else
  * while
  * for
  * break, continue, pass
* Enumerations
  * for loops
  * list comprehensions
  * enumerate
  * zip
* Functions
  * Declaration
  * Calling
  * Keyword arguments
* Object orientation
  * Classes
  * Methods
  * Properties (instance variables)
  * self
* Modules
  * import
  * aliasing (`import pandas as pd`)
  * global import (`from pandas import *`)
* IO
  * Read a file
  * Write to a file

Test yourself with these questions:

1. What's the difference between a list and a generator? And the advantages of either?
2. What is the advantage of storing a word list in a set rather than a list?
