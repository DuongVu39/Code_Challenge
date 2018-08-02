# Environmental Code Challenge

Jul 18th, 2018

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

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python version](https://img.shields.io/badge/Python-%3E3.6-ffdd1c.svg)](https://www.python.org/)

</a></h4>

<h1></h1>
<h4 align="center">
<a href="#notebook">Notebook</a> &nbsp;•&nbsp; <a href="#main-features">Main Features</a>&nbsp;&nbsp;•&nbsp;  <a href="#usage">Usage</a>&nbsp;&nbsp;•&nbsp;<a href="#dependencies">Dependencies</a> •&nbsp;<a href="#folder-structure">Folder Structure</a> &nbsp;&nbsp;

</h4>

<br>

## Overview



#### Task 1 - Classify wind turbine failure

<h4 align="center">
  <br>

![](assets/wind_turbine.jpg)

Classify if the turbine will break down within the next 40 days

<br></h4>

[`predictive_maintenance_dataset.csv`](data/predictive_maintenance_dataset.csv) is a file that contains parameters and settings for many wind turbines: 

- operational_setting_1
- operational_setting_2
- sensor_measurement_1
- sensor_measurement_2 ...

There is a column called `unit_number` which specifies which turbine it is, and one called `status`, in which a value of 1 means the turbine broke down that day, and 0 means it didn't. 

The task is to create a model that, when fed with operational  settings and sensor measurements (unit_number and time_stamp will not be  fed in), outputs 1 if the turbine will break down within the next 40  days, and 0 if not.

For a closer look at the process, please review the [Jupyter Notebook](src/task1/Task1.ipynb)

#### Task 2 - Predict city pollution

<h4 align="center">
  <br>

![](assets/polution.PNG)

Predict the pollution value after 6 hours. 
<br>
</h4>

[`forecasting_dataset.csv`](data/forecasting_dataset.csv) is a file that contains pollution data for a  city. The task is to create a model that, when fed with columns co_gt,  nhmc, c6h6, s2, nox, s3, no2, s4, s5, t, rh, ah, and level, predicts the value of y six hours later. 

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

- Get dummies from categorical variable and drop 1 level
- Select only features appears in training set
- Impute with the mean
- Feed Forward Neural Network with Keras



Task 2 pipeline contains:

- Select only features appears in training set
- Get dummies from categorical variable
- Impute with the mean
- Feed Forward Neural Network with Keras



## Usage

Download the model saved in pickle file in [Result](results/) folder.

**For task 1:**

- Load in the pipeline first
- Then load the keras model in the pipeline. (use **Keras 1.2** to load the model)

```
# Load the pipeline first:
pl_load_in = joblib.load('../../results/task1_pipeline.pkl')

# Then, load the Keras model:
pl_load_in.named_steps['model'].model = load_model('../../results/task1_keras_model.h5')

# Test the model:
# Compute and print MSE for validation
ypred = pl_load_in.predict(Xval)
mse = mean_squared_error(yval, ypred)
print("Mean squared error: %f" % (mse))

# reset index for comparison (if yval already have clean index, this step can be omitted)
yval2 = yval.reset_index(drop=True)

# assign hard label (function hard_label() is in src.task1.reform_results)
new_ypred=pd.DataFrame(ypred)[0].apply(hard_label)

# Compute the accuracy: accuracy for validation
accuracy = float(np.sum(new_ypred==yval2))/yval2.shape[0]
print("accuracy: {}%".format(round(accuracy*100, 3)))
```



**For task 2:**

Load in the pipeline. The model is included in the pipeline.

```
# load the model from disk
filename = 'results/task2_model.pkl' # path leads to pickle model
loaded_model = pickle.load(open(filename, 'rb'))

# Test the model
ypred = loaded_model.predict(Xtest)
print("R squared score is:", r2_score(ytest,ypred).round(3))
```



## Dependencies

- numpy
- pandas
- missingno
- imbalanced-learn
- sklearn
- statsmodels
- keras 2.0 for modelling, 1.2 if just need to load model and use it.
- matplotlib
- seaborn
- scikitplot



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
     |-- results		# storing all the result models 
     |-- src                    # source code used for both tasks
     |   -- task1               # code specific for task 1
     |   -- task2               # code specific for task 2
     |-- test			# tests for functions
     |-- assets                 # store images
     |-- bin
     |   -- # keep all the files I want to delete but not sure whether I will need it later
```