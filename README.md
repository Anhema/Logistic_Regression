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
	- [What is a Logistic Regression](#what-is-a-logistic-regression)
- [Project Subject](#project-subject)
	- [Objectives](#objectives)
	- [General Instructions](#general-instructions)
	- [Mandatory](#mandatory)
		- [Data Analysis](#data-analysis)
		- [Data Visualization](#data-visualization)
		- [Logistic Regression](#logistic-regression-1)
	- [Bonus](#bonus)

## Logistic Regression

### What is a Logistic Regression?

Logistic regression is a process of modeling the probability of a discrete outcome given an input variable.

Multinomial logistic regression can model scenarios where there are more than two possible discrete outcomes. Logistic regression is a useful analysis method for classification problems, where you are trying to determine if a new sample fits best into a category.

The logistic regresion is used in medical an social science. Other names for logistic regression used in other aplication areas are **logistic model, logit model and maximun entropy classifier.**

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
<br>
<br>

<h4 align="center">A minimal Markdown Editor desktop app built on top of <a href="http://electron.atom.io" target="_blank">Electron</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
	<img src="https://badge.fury.io/js/electron-markdownify.svg"
		 alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
	  <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
	<img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif)

## Key Features

* LivePreview - Make changes, See changes
  - Instantly see what your Markdown documents look like in HTML as you create them.
* Sync Scrolling
  - While you type, LivePreview will automatically scroll to the current location you're editing.
* GitHub Flavored Markdown  
* Syntax highlighting
* [KaTeX](https://khan.github.io/KaTeX/) Support
* Dark/Light mode
* Toolbar for basic Markdown formatting
* Supports multiple cursors
* Save the Markdown preview as PDF
* Emoji support in preview :tada:
* App will keep alive in tray for quick usage
* Full screen mode
  - Write distraction free.
* Cross platform
  - Windows, macOS and Linux ready.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/amitmerchant1990/electron-markdownify

# Go into the repository
$ cd electron-markdownify

# Install dependencies
$ npm install

# Run the app
$ npm start
```

> **Note**
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.


## Download

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## Emailware

Markdownify is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <bullredeyes@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [Electron](http://electron.atom.io/)
- [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)
- [showdown](http://showdownjs.github.io/showdown/)
- [CodeMirror](http://codemirror.net/)
- Emojis are taken from [here](https://github.com/arvida/emoji-cheat-sheet.com)
- [highlight.js](https://highlightjs.org/)

## Related

[markdownify-web](https://github.com/amitmerchant1990/markdownify-web) - Web version of Markdownify

## Support

<a href="https://www.buymeacoffee.com/5Zn8Xh3l9" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)

