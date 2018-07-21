# Code Challenge for Canvas Analytics

Jul 2018

<h4 align="center">
  <br>
Classification and prediction project
<br>
</h1>

<h5 align="center">
Created by</a></h5>

<h4 align="center">

[Duong Vu](https://github.com/DuongVu39)

</a></h4>

<br>
<h4 align="center">



<br>
<h4 align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

</a></h4>

<h1></h1>
<h4 align="center">
  <a href="#main-features">Main Features</a> &nbsp;&nbsp;&nbsp;•&nbsp;
  <a href="#Usage">Usage</a> &nbsp;&nbsp;&nbsp;•&nbsp;
  <a href="#Dependencies">Dependencies</a> &nbsp;&nbsp;
</h4>

<br>

## Overview



#### Task 1 - Classify wind turbine failure

<h4 align="center">![](D:/Job/Code%20Challenge/Canvas%20Analytics/Code_Challenge/assets/wind_turbine.jpg)</h4>

Classify if the turbine will break down within the next 40 days



#### Task 2 - Predict city pollution

<h4 align="center">![](D:/Job/Code%20Challenge/Canvas%20Analytics/Code_Challenge/assets/polution.PNG)</h4>

Predict the pollution value after 6 hours. 

### Notebook

A writeup explaining any significant design decisions and your reasons for making them: [Notebook](doc/notebook.md)



## Main Features

The model is actually a pipeline for both tasks which contains:

- Select only features appears in training set
- Impute with the mean
- Get dummies from categorical variable and drop 1 level
- Feed Forward Neural Network with Keras



## Usage





## Dependencies

- numpy
- pandas
- missingno
- imbalanced-learn
- sklearn
- keras
- matplotlib
- seaborn



### Folder Structure

The hierarchy template will look like this:

```
     .
     |-- README 
     |-- LICENSE
     |-- .gitignore.py        
     |-- data
     |   -- predictive_maintenance_dataset.csv
     |   -- forecasting_dataset.csv
     |-- doc 
     |   -- notebook.md         # electronic lab notebook recording your experiments
     |   -- manuscript.md       
     |-- results
     |-- src                    # source code
     |-- test				   # tests for functions
     |-- assets                 # store images
     |-- bin
     |   -- # keep all the files you want to delete but not sure whether you will need it later
```