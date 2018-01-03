""" This script accepts the dataset and acts like a tool to analyze the data quality.
It is well documented with comments and readable/user friendly as takes a functional approach.
It contains auxillary functions to generate some important charts and visuals which shall be required for analysis.

1) analyze_basic_quality: Calculates standard data quality metric
2) analyze_flying_etiquette: Applies the above function#1 to all the columns of the concerned data
3) plot_one_column: Plots one column after accepting data along with colum header information
4) plot_all_columns: Plots all the columns one by one by running the above function#3 to all the columns in the data
"""

# Essential library imports
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

# Defining Auxillary functions and classes

def replaceNA(x):
	if pd.isnull(x):
		return(-5)
	else:
		return(x)

def analyze_basic_quality(data,header_value):
    # Filtering data based on header value specified and taking the count of values
    filtered_data=data[[header_value]]
    print("Total number of entries= ",len(filtered_data.index),"\n")
    # Getting the list of values in the column
    list_of_values=list((filtered_data[header_value]).values)
    # Getting the unique set of values
    unique_list_of_values=set(list_of_values)
    # Printing number of duplicates
    print("Number of Unique values= ",len(unique_list_of_values),"\n")
    print("No of duplicates= ",len(list_of_values)-len(unique_list_of_values),"\n")
    # check for NAs
    filtered_data['na_values']=filtered_data[header_value].apply(replaceNA)
    na_filtered_data=filtered_data[filtered_data['na_values']==-5]
    print("No of NA values= ",len(na_filtered_data.index),"\n")


def analyze_flying_etiquette(data):
    list_of_headers=list(data)
    # Calling the quality check function on each header
    # Attempting to store output in a text file
    sys.stdout=open("quality_analysis_flying_etiquette.txt","w")
    # Running the quality analysis code
    ctr=1
    for val in list_of_headers:
        print("\n\n")
        print("SNo: ",ctr,"\n")
        print("Header Value=",val,"\n")
        analyze_basic_quality(data,val)
        print("\n\n")
        ctr+=1
    # Closing the functionality of printing to a file
    sys.stdout.close()

def plot_one_column(data,header_value):
	values=(data[header_value]).tolist()
	dict_of_values=Counter(values)
	key_values=[]
	data_values=[]
	blank_present=0
	for (key,val) in dict_of_values.items():
		if pd.isnull(key):
			blank_value,blank_present=val,1
			continue
		key_values.append(key)
		data_values.append(val)
	# Sorting the values for the graph
	mix=zip(data_values,key_values)
	sorted_mix=sorted(mix)
	data_values=[val[0] for val in sorted_mix]
	key_values=[val[1] for val in sorted_mix]
	# To put the blank values at the first/bottom of the graph
	if blank_present==1:
		key_values.insert(0,"Blank/Empty Response")
		data_values.insert(0,blank_value)
	# Preparing to plot
	y_pos = np.arange(len(key_values))
	plt.barh(y_pos,data_values ,align='center')
	# Attaching labels
	for i, v in enumerate(key_values):
		plt.text(data_values[key_values.index(v)]-2,i,str(v), color='blue', fontweight='bold', fontsize="10")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Type of Response')
	plt.xlabel('Counts')
	plt.title('"%s"'%(header_value))
	plt.show()
	for (key,value) in sorted_mix:
		print(key,"\n\n",value)
		print("\n")

def plot_all_columns(data):
	list_of_headers=list(data)
	for val in list_of_headers:
		plot_one_column(data,val)

def main():
	# Establishing path to data which is a directory below/inside
	current_path=os.path.abspath(__file__)
	parent_path=os.path.abspath(os.path.join("."))
	path_to_data=os.path.abspath(os.path.join(parent_path,'Data/flying_etiquette.csv'))
	# loading the data
	flying_survey_data=pd.read_csv(path_to_data,low_memory=False)
	# Analyze Complete Quality of flying-etiquette data
	analyze_flying_etiquette(flying_survey_data)
	# Analyze individual charts of the data
	#plot_one_column(flying_survey_data,"Have you ever smoked a cigarette in an airplane bathroom when it was against the rules?")
	# Analyze all the columns by plotting each column
	plot_all_columns(flying_survey_data)

if __name__=="__main__":
    main()
