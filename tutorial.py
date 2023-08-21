'''
Prepare the pandas library
Python version 3.8 is the most stable version, used in the different tutorials

python3 --version
pip3 --version
pip3 install pandas
'''

# assume you have your data stored in a .csv file somewhere on your computer, the first step is to load and read such data
# for these tutorials, we will generate data using https://www.mockaroo.com or https://cobbl.io and test the different functions offered by the libraries we imported


import pandas as pd

data = pd.read_csv('employeeInfo.csv', header=0)   # let's load the dataset

print(data.info())     # let's print statistical info about the dataset
print(data.head())     # let's print the header along with the first 5 rows




# Let's read the salary of the first 15 rows of our dataset, and mark the header to be row number 1
data = pd.read_csv('employeeInfo.csv',
        header=0,
        nrows = 15,
        usecols=["Salary"])


employeeNumber= 0
data = data.to_string().splitlines()

# Using for loop to process each salary individually
# We would like also to skip the first row, which carries the name of the column

for salary in data[1:]:
    employeeNumber = employeeNumber + 1
    print("Employee Number:", employeeNumber, " with Salary:", salary)
