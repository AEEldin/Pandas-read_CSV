# Pandas work with CSV files
In this tutorial, we will discuss using Python's Pandas library to parse and read CSV files, as a first step in cleaning your dataset.


## Prepare the Pandas and Numpy libraries.

This tutorial is using Python version 3.8, as a very stable version. With a ready Python on your computer, check the following commands:

> python3 --version

> pip3 --version

> pip3 install pandas

> pip3 install numpy

Create a .py file, import the library, and you can also check the version of the libraries as follows:

```
import pandas                # first step is to import both Pandas and NumPy libraries
import numpy                
print(pandas.__version__)    # let's then check the version used
print(numpy.__version__)    
```

The read_csv() is the primary function we will use in this tutorial, this function provides a wide set of functions that we will utilize to work with CSV files (our dataset).

```
import pandas as pd   # let's import pandas with an alias of pd
import numpy as np    # let's import numpy with an alias of np
```



## Part 1: loading and read your dataset

Assume you have your data stored in a .csv file somewhere on your computer; the first step is to load and read such data. For these tutorials, we will generate data using https://www.mockaroo.com or https://cobbl.io and test the different functions offered by the libraries we imported. Our dataset is named employeeInfo.csv and stores randomly generate information about employees (e.g., names, addresses, salaries, IDs, emails)

```
import pandas as pd  

data = pd.read_csv('employeeInfo.csv')       # use pandas's read_csv() function to load your dataset
print(data)                                  # print your data using the print() function
```

In order to print the entire file, you can simply use the print(); however, with a large data set with many rows, Pandas will only return the first 5 and last 5 rows.
```
print(data)                                  # the data is of type <class 'pandas.core.frame.DataFrame'>
print(data.to_string())                      # you can convert the data into string
```

In order to get some statistical information about your dataset, you can use the info() function. The statistical information includes the number of rows and columns, the names of the fields (columns), and the data type of each field
```
print(data.info())
```



## Part 2: working with the header and the separator

The read_csv() function also accepts a header parameter (default = 0) that indicates that the header starts from the first row (index of 0). 
```
data = pd.read_csv('employeeInfo.csv', header=0)  # gives the same results as pd.read_csv('employeeInfo.csv') 
```

If the headers are on the second row (index of 1) for some reason, you can set header=1 in the read_csv function. However, if your dataset has no header or you would like to deal with the header as a regular row, you can set the header to None
```
data = pd.read_csv('employeeInfo.csv',header = None)
```

By default, CSV files use the comma to separate the values of the different fields. However, in case you are working with a CSV that uses another separator (e.g., ; or |), you should specify such separator using the sep parameter when calling the read_csv() to load your data.

```
data = pd.read_csv('employeeInfo.csv', header=0, sep=';')   
```






## Part3: Reading specific rows from your dataset

Sometimes, you would like to take a look at the structure of the file, here comes the function of head(). The head() function prints the header line and the first 5 rows. The head() function also accepts an integer value indicating how many rows to display from the top
```
print(data.head())           # to print the first 5 rows
print(data.head(10))         # to print the first 10 rows
```

Similar to the head() function, the tail() enable you to read and print the last five rows in the dataset. Tail() also accepts an integer value indicating how many rows to display from the bottom.
```
print(data.tail())           # to print the last 5 rows
print(data.tail(10))         # to print the last 10 rows
```

The read_csv() function also allows the reader to skip certain rows using the _**skiprows**_ parameter. For example, if you would like to skip rows 1,3, 5, and 10:
```
data = pd.read_csv('employeeInfo.csv', skiprows=[1, 3, 5, 10])   
print(data)
```

As another example, if you would like to skip rows from 3 to 14:
```
data = pd.read_csv('employeeInfo.csv', skiprows=range(3,15))    
print(data)
```

You can also skip a certain number of rows from the end of the file using the _**skipfooter**_ parameter of read_csv(). For example, you can skip the last ten rows of your dataset.
```
data = pd.read_csv("employeeInfo.csv", skipfooter=10)
df.tail()
```


Another option, you can read only a certain amount of rows from your dataset using the _**nrows**_ parameter of the read_csv().
```
data = pd.read_csv('employeeInfo.csv', nrows = 25)
```



## Part 4: Reading specific columns of your dataset

In order to get some statistical information about your dataset, you can use the info() function. The statistical information includes the number of rows and columns, the names of the fields (columns), and the data type of each field.
```
print(data.info())
```

We can list the fields (columns) we would like to load, this can be fulfilled using the _**usecols**_ parameter of the read_csv() function

```
data = pd.read_csv('employeeInfo.csv',
        header=0,
        usecols=["First_name", "Email", "Start Date"])

print(data.head())
```

Panadas has -by default- an initial numeric index (you can see it on the far left when you print the data). However, you can set a column to be the index through the _**index_col**_ parameter of the read_csv() function. The index_col parameter accepts a list of columns you would like to choose as indexes.

```
data = pd.read_csv('employeeInfo.csv', header=0, index_col=["Email"])
print(data.head())

data = pd.read_csv('employeeInfo.csv', header=0, index_col=["Email", "State"])
print(data.head())
```


## Part 5: let's put all this together and read the salaries of some employees
We would like to check the salaries column for the first 15 employees

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv',
        header=0,
        nrows = 15,
        usecols=["Salary"])


print("The type of data is:", type(data))

employeeNumber= 0
data = data.to_string().splitlines()

# Using for loop to process each salary individually
# We would like also to skip the first row, which carries the name of the column

for salary in data[1:]:
    employeeNumber = employeeNumber + 1
    print("Employee Number:", employeeNumber, " with Salary:", salary)
```
