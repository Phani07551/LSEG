import os
import random
import pandas as pd



#######################################################################################################################################
def files_validation(exchange_name, number_of_files):
    fileswithpath =[]              
    print ("INFO: Given Exchange Name is "+ exchange_name +" and Number of Files are to process is "+ str(number_of_files))

    # list all data files with directory name
    files = os.listdir(exchange_name)

    if files: # Explicitly check if folder empty
        # Genarate the data files with path 
        for file in files:
            fileswithpath.append("./"+exchange_name+"/"+file)

        # Returning the files with full path    
        return fileswithpath
    else:
        print("ERROR: Files not found in the "+ exchange_name)
        quit()
#######################################################################################################################################


#######################################################################################################################################
def get_consecutive_data(file):
    try:
        # read the CSV file from given exchange name
        data = pd.read_csv(file)
        total_data_points = len(data)
        valid_start_indices = list(range(total_data_points - 30))
        # randomly selecting 30 data points 
        start_index = random.choice(valid_start_indices)
        selected_data = data.iloc[start_index:start_index + 30]
        return selected_data
    except pd.errors.EmptyDataError:
        print("Error: The file " + file + " is empty and cannot be read.")
        return pd.DataFrame(columns=['StockID', 'TimeStamp', 'StockPrice'])
    except pd.errors.ParserError:
        print("Error: The file " + file + " contains invalid CSV format or cannot be parsed.")
    except Exception as e:
        print("Error: An unexpected error occurred:"+e)
#######################################################################################################################################

#######################################################################################################################################
def detect_outliers(data):
    # Adding columns names to existed data 
    data.columns =['StockID', 'TimeStamp', 'StockPrice']
    prices = data['StockPrice']

    mean_price = prices.mean()
    std_dev = prices.std()

    threshold_upper = mean_price + 2 * std_dev
    threshold_lower = mean_price - 2 * std_dev

    outliers = data[(prices > threshold_upper) | (prices < threshold_lower)]

    outliers['Mean of 30 Data Points'] = mean_price
    outliers['Deviation from Mean'] = outliers['StockPrice'] - mean_price
    outliers['% Deviation Beyond Threshold'] = (outliers['Deviation from Mean'] / std_dev) * 100

    outliers = outliers[['StockID', 'TimeStamp', 'StockPrice', 'Mean of 30 Data Points', 'Deviation from Mean', '% Deviation Beyond Threshold']]
    return outliers
#######################################################################################################################################

#######################################################################################################################################
def genarate_output(outliers_data, filepath):
    output_folder = "OutPut"
    filepath =  filepath.replace(".csv", "")
    filepath =  filepath.replace("./", "/")
    fullpath = "./"+output_folder+filepath+"_output.csv"

    dir_path = os.path.dirname(fullpath)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Createing the file for output with stock name
    if not os.path.exists(fullpath):
        with open(fullpath, 'w') as file:
            pass  # create the file without any content

    try:
        # Write the data to file
        outliers_data.to_csv(fullpath)
    except PermissionError as e:
        print("PermissionError: File permission error while writing the output")
    except Exception as e:
        print("An error occurred:" +e)
#######################################################################################################################################


# Input the Stocke Exchange Name 
exchange_name = input("INPUT REQUIRED: Enter The Stocke Exchange Name: ")
exchange_name = exchange_name.upper()

# validating Stocke Exchange Name, if it's existed in sample data or not
if not exchange_name:
    print("ERROR: Given " + exchange_name + " Exchange name looks empty")
    exit()   
if not os.path.exists("./"+exchange_name):
    print("ERROR: Given " + exchange_name + " Exchange name is not avalable from sample data")
    exit()


# Input the Number Of Files To Process The Data
number_of_files =  int(input ("INPUT REQUIRED: Enter The Number Of Files To Process The Data from "+exchange_name+": "))

files = files_validation(exchange_name, number_of_files)

for file_count in range(number_of_files):
    if len(files) > file_count:
        print("### INFO: procssing the file " + files[file_count] + " ###")
        consecutive_data = get_consecutive_data(files[file_count])
        if not consecutive_data.empty:
            print("### INFO: 30 consecutive random data points ###")
            print(consecutive_data)
            #if not consecutive_data.empty:
            outliers = detect_outliers(consecutive_data)
            print(outliers)
            genarate_output(outliers, files[file_count])
            



