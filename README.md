# Code Challenge for Canvas Analytics

Jul 2018

<h3 align="center">
Classification and prediction project
<br>
</h3>

<h5 align="center">
<a>Created by</a></h5>

<h4 align="center"><a>

[Duong Vu](https://github.com/DuongVu39)

</a></h4>

<h4 align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

</a></h4>

<h1></h1>
<h4 align="center">
<a href="#notebook">Notebook</a> &nbsp;•&nbsp; <a href="#main-features">Main Features</a>&nbsp;&nbsp;•&nbsp;  <a href="#Usage">Usage</a>&nbsp;&nbsp;•&nbsp;<a href="#Dependencies">Dependencies</a> &nbsp;&nbsp;

</h4>

<br>

## Overview



#### Task 1 - Classify wind turbine failure

<h4 align="center">
  <br>

![](assets/wind_turbine.jpg)

Classify if the turbine will break down within the next 40 days

<br></h4>

For a closer look at the process, please review the [Jupyter Notebook](src/task1/Scratch.ipynb)

#### Task 2 - Predict city pollution

<h4 align="center">
  <br>

![](assets/polution.PNG)

Predict the pollution value after 6 hours. 
<br>
</h4>

For a closer look at the process, please review the [Jupyter Notebook](src/task2/Task2.ipynb)



## Notebook

A writeup explaining design decisions, potential works and the reasons for making current choices: [Notebook](doc/notebook.md)

For log files, open using TensorBoard by typing below command in your terminal in where the log folder is:

```
tensorboard --logdir=logs
```





## Main Features

The model is actually a pipeline for both tasks. 

Task 1 pipeline contains:

- Select only features appears in training set
- Impute with the mean
- Get dummies from categorical variable and drop 1 level
- Feed Forward Neural Network with Keras



Task 2 pipeline contains:

- Select only features appears in training set
- Get dummies from categorical variable
- Impute with the mean
- Feed Forward Neural Network with Keras



## Usage

Download the model saved in pickle file in [Result](results/) folder:

- Load in the pipeline first
- Then load the keras model



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

The hierarchy of this repository is described like below:

```
     .
     |-- README 
     |-- LICENSE
     |-- .gitignore.py        
     |-- data
     |   -- predictive_maintenance_dataset.csv
     |   -- forecasting_dataset.csv
     |-- doc 
     |   -- notebook.md         # electronic lab notebook
     |   -- manuscript.md       
     |-- results
     |-- src                    # source code
     |   -- task1               # code specific for task 1
     |   -- task2               # code specific for task 2
     |-- test			# tests for functions
     |-- assets                 # store images
     |-- bin
     |   -- # keep all the files I want to delete but not sure whether I will need it later
```