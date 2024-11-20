<h3 align="center"> LSEG Test Excution Stpes </h3>
---

# Table of Content

- [Prerequisite](#Prerequisite)
- [Installation](#Installation)
- [ExecutionSteps](#ExecutionSteps)
- [Output](#Output)
- [NOTE](#NOTE)

# Prerequisite <a name = Prerequisite></a>
Before running the Python scripts, make sure you have the following installed:

1. Python 3.x: Make sure you are using Python 3. You can download the latest version from python.org.
2. install pandas with pip command:
> pip install pandas


## Installation <a name = Installation></a>
First, clone this repository to your local machine using git. Open a terminal and run the following command:

> git clone https://github.com/Phani07551/LSEG.git

## ExecutionSteps <a name = ExecutionSteps></a>
1. Once you've installed the python3 and pandas, you are ready to run the scripts.
2. you have to run the script called LSEG-test.py

    > python3 LSEG-test.py

3. it will ask for first input of stock exchange name, as per sample data we have to give any one of input like below
    > LSE

    or
    > NASDAQ

    or
    > NYSE

4. it will ask for second input as Number Of Files To Process The Data, we can give nay number more then zero.
    NOTE: Based on input number of files will process, if sample data have two files in the exchange name and input values is more then two it will process the maximum number files in the exchange until input value
    > 1


# Output <a name = Output></a>
As per requirment: 
1. 1st function will print the 0 consecutive data points starting from a random timestamp within the file on the commandline
2. 2nd function output will genarate in the path ./Output/<exchangename>/stockname_output.csv 
> example: ./Output/LSE/FLTRLSE_output.csv



# NOTE <a name = NOTE></a>
1. All the sample data given for test available in the repo
2. if we anted to try script with diffrent exchange name, we have to run the script again and provide the inputs like exchange name and number of files to process