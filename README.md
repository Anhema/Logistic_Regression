<h1 align="center">
	<br>
		<img src="https://cdn-icons-png.flaticon.com/128/1998/1998661.png" alt="Logistic Regression" width="200">
	<br>
		LOGISTIC REGRESSION
	<br>
</h1>
<br>

## Index
- [Logistic Regression](#logistic-regression)
	- [What is a Logistic Regression?](#what-is-a-logistic-regression)
	- [Whow does the Logistic Regression works?](#whow-does-the-logistic-regression-works)
- [Project Subject](#project-subject)
	- [Objectives](#objectives)
	- [General Instructions](#general-instructions)
	- [Mandatory](#mandatory)
		- [Data Analysis](#data-analysis)
		- [Data Visualization](#data-visualization)
		- [Logistic Regression](#logistic-regression-1)
	- [Bonus](#bonus)
- [Terminologies](#terminologies)

## Logistic Regression

### What is a Logistic Regression?

Logistic regression is a process of modeling the probability of a discrete outcome given an input variable.

Multinomial logistic regression can model scenarios where there are more than two possible discrete outcomes. Logistic regression is a useful analysis method for classification problems, where you are trying to determine if a new sample fits best into a category.

The logistic regresion is used in medical an social science. Other names for logistic regression used in other aplication areas are **logistic model, logit model and maximun entropy classifier.**

Logistic Regresion predicts the output of a categorical dependent variable. Therefore, theoutcome must be a categorical or discrete value.
Instead of fitting a regression line, we fit a "S" shaped logidtic function, which predicts two maximun values (0 or 1).
These prediction give aprobabilistic values which lie between Yes or No.

![Logistic Regression image](https://miro.medium.com/v2/resize:fit:1184/1*XJHhJLWWzB5vP2PmyXybJg.png)

Like in linear regression, we can make simple models (Obesity is predicted by Weight) or more complicated models (Obesity is predicted by Weight + Genotype + Age + Astrological Sign). We can also test to see if each variable is useful for predicting (Obesity is predicted by Weight + Genotype + Age + Astrological Sign here Astrological Sign is not helping the prediction).

### Whow does the Logistic Regression works?

#### Data Reading

First we should get the all dataset. The data should be in a format where each row represents a single observation and each column represents a different variable. The target variable should be binary.



## Project Subject

### Objectives

The main objective for this project is the implementaion of a Logistic Regression as a continuation of the [Linear Regression](https://github.com/Anhema/Linear_Regression) project.

Also learn how to read a data set, to visualize it in different ways, to select and clear unnecesary information from your data.

### General Instructions

In order to learn how to read data any fuction that do all the heavy-lifting for you (describe function of *pandas*, fore example)

### Mandatory

#### Data Analysis

First of all, take a look at the available data. look in what format it is presented, if
there are various types of data, the different ranges, and so on. It is important to make
an idea of your raw material before starting. The more you work on data - the more you
develop an intuition about how you will be able to use it.
In this part, Professor McGonagall asks you to produce a program called describe.[extension].
This program will take a dataset as a parameter. All it has to do is to display information
for all numerical features like in the example:

```bash
$> describe.[extension] dataset_train.csv
		Feature 1   Feature 2   Feature 3   Feature 4
Count   149.000000  149.000000  149.000000  149.000000
Mean    5.848322	3.051007	3.774497	1.205369
Std     5.906338    3.081445	4.162021	1.424286
Min		4.300000	2.000000	1.000000	0.100000
25%		5.100000	2.800000	1.600000	0.300000
50%		5.800000	3.000000	4.400000	1.300000
75%		6.400000	3.300000	5.100000	1.800000
Max		7.900000	4.400000	6.900000	2.500000
```

#### Data visualization

Data visualization is a powerful tool for a data scientist. It allows you to make insights
and develop an intuition of what your data looks like. Visualizing your data also allows
you to detect defects or anomalies.


-  Histogramm
	-	Make a script called histogram.[extension] which displays a histogram answering the
next question :
Which Hogwarts course has a homogeneous score distribution between all four houses?
-	Scatter plot
	- Make a script called scatter_plot.[extension] which displays a scatter plot answering
the next question :
What are the two features that are similar ?
-	Pair plot
	- Make a script called pair_plot.[extension] which displays a pair plot or scatter plot
matrix (according to the library that you are using).
From this visualization, what features are you going to use for your logistic regression?

#### Logistic Regression

You arrive at the last part: code your Magic Hat. To do this, you have to perform a
multi-classifier using a logistic regression one-vs-all.

You will have to make two programs :
- First one will train your models, it’s called logreg_train.[extension]. It takes
as a parameter dataset_train.csv. . For the mandatory part, you must use the
technique of gradient descent to minimize the error. The program generates a file
containing the weights that will be used for the prediction.
- A second has to be named logreg_predict.[extension]. It takes as a parameter
dataset_test.csv and a file containing the weights trained by previous program.
In order to evaluate the performance of your classifier this second program will have
to generate a prediction file houses.csv formatted exactly as follows:

```bash
$> cat houses.csv
Index,Hogwarts House
0,Gryffindor
1,Hufflepuff
2,Ravenclaw
3,Hufflepuff
4,Slytherin
5,Ravenclaw
6,Hufflepuff
[...]
```

### Bonus

- Add more fields for **describe.[extension]**
- Implement a *Stochastic gradiont descent*
- Implement othe optimization algorithms (Match GD/mini-batch GD/ ...)

<br>
<br>
<br>

## Terminologies

- **Independent variables**: The input characteristics or predictor factors applied to the predictions of the dependent varialble.
- **Dependent variables**: The objective variables we are trying to predict.
- **Logistic Function**: The used formula to represent how does the independent variables and the dependent variables are related. The logistic function transform the input variables in a value between 0 and 1.
- **Probabilities**: Is the ratio of something that happens to something that not happens. Is different from probability, is the ratio of something occurring to everything that could possibly occur.
- **Log-odds**: The log-odds, also known as the logit function, is the natural logarithm of the odds. In logistic regression, the log odds of the dependent variable are modeled as a linear combination of the independent variables and the intercept.
- **Coefficient**: 
- **Intercept**: 
- **Maximun Likehood estimation**:
