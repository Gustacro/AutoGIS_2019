# Exercise 3

This week we will practice how to do geocoding, spatial joins and nearest neighbour analysis in Python. 

In this exercise, we will work with a practical case: the goal is to **find out how many people live within 1.5 km (Euclidian) distance from big shopping centers in Helsinki Region**, and which of those shopping centers is closest to your home and work location (Problems 1-3). In addition, you will figure out the closes shopping center from your home and work locations (Problem 4). 


- **Exercise 3 is due by Wednesday the 20th of November at 4pm** (day before the next practical session).


- Hints will be added [here](https://automating-gis-processes.github.io/site/lessons/L3/exercise-3.html) if needed. Remember also to ask for help if our Slack channel!

- Scores on this exercise are out of **20 points**.

## Sections

 - [Problem 1: Geocode shopping centers](Exercise-3-Problem-1-3.ipynb#problem-1-geocode-shopping-centers-5-points)
 - [Problem 2: Create buffers around shopping centers](Exercise-3-Problem-1-3.ipynb#problem-2-create-buffers-around-shopping-centers-5-points)
 - [Problem 3: How many people live near shopping centers?](Exercise-3-Problem-1-3.ipynb#problem-3-how-many-people-live-near-shopping-centers-5-points)
 - [Problem 4: What is the closest shopping center from your home / work?](Exercise-3-Problem-4)
 
 
 ## Solution cells and test cells

#### Solution code cells
You can always start working by removing these two lines of comments/code: 

```
# YOUR CODE HERE
raise NotImplementedError()
```
We are checking your solutions semi-automatically using [nbgrader](https://nbgrader.readthedocs.io/en/stable/index.html#) which is a package for creating and grading assingments in Jupyter Notebooks. Please use the suggested variable names when writing your code so that our hidden tests work smoothly :)

#### Non-editable code cells
Some of the code-cells are "non-editable" which means that you are supposed to run them, but you are not able to edit them. These Non-editable code cells should help you to test your code while you proceed. 

 
