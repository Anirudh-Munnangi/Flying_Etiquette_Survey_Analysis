""" This script accepts the dataset and acts like a tool to analyze some mixed comparative insights.
It is well documented with comments and readable/user friendly as takes a functional approach.
It contains auxillary functions to generate some important charts and visuals which shall be required for analysis.
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

def compare_gender_and_unrulykids(data):
	gender_values=list((data['Gender']).values)
	unrulykids_values=list((data['In general, is it rude to knowingly bring unruly children on a plane?']).values)
	mixed_values=list(zip(gender_values,unrulykids_values))
	nonnull_unrulykids_gender_male=[unrulykids for (gender,unrulykids) in mixed_values if ((pd.isnull(gender) is False) and (pd.isnull(unrulykids) is False) and gender=='Male')]
	nonnull_unrulykids_gender_female=[unrulykids for (gender,unrulykids) in mixed_values if ((pd.isnull(gender) is False) and (pd.isnull(unrulykids) is False) and gender=='Female')]
	keys_actual=['Yes, very rude','Yes, somewhat rude','No, not at all rude']
	counter_gender_male=Counter(nonnull_unrulykids_gender_male)
	counter_gender_female=Counter(nonnull_unrulykids_gender_female)
	values_gender_male=[counter_gender_male[val] for val in keys_actual]
	values_gender_female=[counter_gender_female[val] for val in keys_actual]

	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(2)
	bar_width = 0.2
	opacity = 0.8
	# Grouping the plot values
	values1=[values_gender_male[0],values_gender_female[0]]
	values2=[values_gender_male[1],values_gender_female[1]]
	values3=[values_gender_male[2],values_gender_female[2]]
	values1=[190,158]
	values2=[155,193]
	values3=[56,91]
	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Yes, very rude')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='r',label='Yes, somewhat rude')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, values3, bar_width,alpha=opacity,color='g',label='No, not at all rude')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Male','Female'))
	plt.title('In general, is it rude to knowingly bring unruly children on a plane?')
	plt.legend()
	plt.tight_layout()
	plt.show()


def compare_gender_and_babies(data):
	gender_values=list((data['Gender']).values)
	babies_values=list((data['In general, is it rude to bring a baby on a plane?']).values)
	mixed_values=list(zip(gender_values,babies_values))
	nonnull_babies_gender_male=[babies for (gender,babies) in mixed_values if ((pd.isnull(gender) is False) and (pd.isnull(babies) is False) and gender=='Male')]
	nonnull_babies_gender_female=[babies for (gender,babies) in mixed_values if ((pd.isnull(gender) is False) and (pd.isnull(babies) is False) and gender=='Female')]
	keys_actual=['Yes, very rude','Yes, somewhat rude','No, not at all rude']
	counter_gender_male=Counter(nonnull_babies_gender_male)
	counter_gender_female=Counter(nonnull_babies_gender_female)
	values_gender_male=[counter_gender_male[val] for val in keys_actual]
	values_gender_female=[counter_gender_female[val] for val in keys_actual]

	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(2)
	bar_width = 0.2
	opacity = 0.8
	# Grouping the plot values
	values1=[values_gender_male[0],values_gender_female[0]]
	values2=[values_gender_male[1],values_gender_female[1]]
	values3=[values_gender_male[2],values_gender_female[2]]
	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Yes, very rude')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='r',label='Yes, somewhat rude')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, values3, bar_width,alpha=opacity,color='g',label='No, not at all rude')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Male','Female'))
	plt.title('In general, is it rude to bring a baby on a plane?')
	plt.legend()
	plt.tight_layout()
	plt.show()



def compare_gender_and_talking(data):
	gender_values=list((data['Gender']).values)
	talking_values=list((data['Generally speaking, is it rude to say more than a few words tothe stranger sitting next to you on a plane?']).values)
	mixed_values=list(zip(gender_values,talking_values))
	nonnull_talking_gender_male=[talking for (gender,talking) in mixed_values if ((pd.isnull(gender) is False) and (pd.isnull(talking) is False) and gender=='Male')]
	nonnull_talking_gender_female=[talking for (gender,talking) in mixed_values if ((pd.isnull(gender) is False) and (pd.isnull(talking) is False) and gender=='Female')]
	keys_actual=['Yes, very rude','Yes, somewhat rude','No, not at all rude']
	counter_gender_male=Counter(nonnull_talking_gender_male)
	counter_gender_female=Counter(nonnull_talking_gender_female)
	values_gender_male=[counter_gender_male[val] for val in keys_actual]
	values_gender_female=[counter_gender_female[val] for val in keys_actual]

	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(2)
	bar_width = 0.2
	opacity = 0.8
	# Grouping the plot values
	values1=[values_gender_male[0],values_gender_female[0]]
	values2=[values_gender_male[1],values_gender_female[1]]
	values3=[values_gender_male[2],values_gender_female[2]]
	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Yes, very rude')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='r',label='Yes, somewhat rude')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, values3, bar_width,alpha=opacity,color='g',label='No, not at all rude')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Male','Female'))
	plt.title('Is it rude to say a few words to a stranger')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_age_and_bathroom(data):
	age_values=list((data['Age']).values)
	bathroom_values=list((data['Is it rude to wake a passenger up if you are trying to go to the bathroom?']).values)
	mixed_values=list(zip(age_values,bathroom_values))
	nonnull_bathroom_preference_age_18_29=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='1')]
	nonnull_bathroom_preference_age_30_44=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='3')]
	nonnull_bathroom_preference_age_45_60=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='4')]
	nonnull_bathroom_preference_age_gt_60=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='>')]
	keys_actual=['Yes, very rude','Yes, somewhat rude','No, not at all rude']
	counter_age_18_29=Counter(nonnull_bathroom_preference_age_18_29)
	counter_age_30_44=Counter(nonnull_bathroom_preference_age_30_44)
	counter_age_45_60=Counter(nonnull_bathroom_preference_age_45_60)
	counter_age_gt_60=Counter(nonnull_bathroom_preference_age_gt_60)
	values_age_18_29=[counter_age_18_29[val] for val in keys_actual]
	values_age_30_44=[counter_age_30_44[val] for val in keys_actual]
	values_age_45_60=[counter_age_45_60[val] for val in keys_actual]
	values_age_gt_60=[counter_age_gt_60[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(4)
	bar_width = 0.2
	opacity = 0.8
	# Grouping the plot values
	values1=[values_age_18_29[0],values_age_30_44[0],values_age_45_60[0],values_age_gt_60[0]]
	values2=[values_age_18_29[1],values_age_30_44[1],values_age_45_60[1],values_age_gt_60[1]]
	values3=[values_age_18_29[2],values_age_30_44[2],values_age_45_60[2],values_age_gt_60[2]]

	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Yes, very rude')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='g',label='Yes, somewhat rude')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, values3, bar_width,alpha=opacity,color='r',label='No, not at all rude')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Age: 18-29','Age: 30-44','Age: 45-60','Age: > 60',))
	plt.title('Is it rude to wake a passenger up if you are trying to go to the bathroom?')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_age_and_reclinepreference(data):
	age_values=list((data['Age']).values)
	reclinepreference_values=list((data['Do you ever recline your seat when you fly?']).values)
	mixed_values=list(zip(age_values,reclinepreference_values))
	nonnull_recline_preference_age_18_29=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='1')]
	nonnull_recline_preference_age_30_44=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='3')]
	nonnull_recline_preference_age_45_60=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='4')]
	nonnull_recline_preference_age_gt_60=[preference for (age,preference) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(preference) is False) and age[0]=='>')]
	keys_actual=['Once in a while','Usually','Never','Always','About half the time']
	counter_age_18_29=Counter(nonnull_recline_preference_age_18_29)
	counter_age_30_44=Counter(nonnull_recline_preference_age_30_44)
	counter_age_45_60=Counter(nonnull_recline_preference_age_45_60)
	counter_age_gt_60=Counter(nonnull_recline_preference_age_gt_60)
	values_age_18_29=[counter_age_18_29[val] for val in keys_actual]
	values_age_30_44=[counter_age_30_44[val] for val in keys_actual]
	values_age_45_60=[counter_age_45_60[val] for val in keys_actual]
	values_age_gt_60=[counter_age_gt_60[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(4)
	bar_width = 0.1
	opacity = 0.8
	# Grouping the plot values
	values1=[values_age_18_29[0],values_age_30_44[0],values_age_45_60[0],values_age_gt_60[0]]
	values2=[values_age_18_29[1],values_age_30_44[1],values_age_45_60[1],values_age_gt_60[1]]
	values3=[values_age_18_29[2],values_age_30_44[2],values_age_45_60[2],values_age_gt_60[2]]
	values4=[values_age_18_29[3],values_age_30_44[3],values_age_45_60[3],values_age_gt_60[3]]
	values5=[values_age_18_29[4],values_age_30_44[4],values_age_45_60[4],values_age_gt_60[4]]

	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Once in a while')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='g',label='Usually')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, values3, bar_width,alpha=opacity,color='r',label='Never')
	#Plot 4
	rects4 = plt.bar(index+3*bar_width, values4, bar_width,alpha=opacity,color='y',label='Always')
	#Plot 5
	rects5 = plt.bar(index+4*bar_width, values5, bar_width,alpha=opacity,color='c',label='About half the time')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Age: 18-29','Age: 30-44','Age: 45-60','Age: > 60',))
	plt.title('Do you ever recline your seat when you fly?')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_age_and_reclinerudeness(data):
	age_values=list((data['Age']).values)
	reclinerudeness_values=list((data['Is it rude to recline your seat on a plane?']).values)
	mixed_values=list(zip(age_values,reclinerudeness_values))
	nonnull_recline_rudeness_age_18_29=[rudeness for (age,rudeness) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(rudeness) is False) and age[0]=='1')]
	nonnull_recline_rudeness_age_30_44=[rudeness for (age,rudeness) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(rudeness) is False) and age[0]=='3')]
	nonnull_recline_rudeness_age_45_60=[rudeness for (age,rudeness) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(rudeness) is False) and age[0]=='4')]
	nonnull_recline_rudeness_age_gt_60=[rudeness for (age,rudeness) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(rudeness) is False) and age[0]=='>')]
	keys_actual=['Yes, very  rude','Yes, somewhat rude','No, not rude at all']
	counter_age_18_29=Counter(nonnull_recline_rudeness_age_18_29)
	counter_age_30_44=Counter(nonnull_recline_rudeness_age_30_44)
	counter_age_45_60=Counter(nonnull_recline_rudeness_age_45_60)
	counter_age_gt_60=Counter(nonnull_recline_rudeness_age_gt_60)
	values_age_18_29=[counter_age_18_29[val] for val in keys_actual]
	values_age_30_44=[counter_age_30_44[val] for val in keys_actual]
	values_age_45_60=[counter_age_45_60[val] for val in keys_actual]
	values_age_gt_60=[counter_age_gt_60[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(4)
	bar_width = 0.1
	opacity = 0.8
	# Grouping the plot values
	values1=[values_age_18_29[0],values_age_30_44[0],values_age_45_60[0],values_age_gt_60[0]]
	values2=[values_age_18_29[1],values_age_30_44[1],values_age_45_60[1],values_age_gt_60[1]]
	values3=[values_age_18_29[2],values_age_30_44[2],values_age_45_60[2],values_age_gt_60[2]]

	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Yes, very rude')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='g',label='Yes, somewhat rude')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, values3, bar_width,alpha=opacity,color='r',label='No, not rude at all')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Age: 18-29','Age: 30-44','Age: 45-60','Age: > 60',))
	plt.title('Is it rude to recline your seat')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_age_and_reclineelimination(data):
	age_values=list((data['Age']).values)
	reclineelimination_values=list((data['Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?']).values)
	mixed_values=list(zip(age_values,reclineelimination_values))
	nonnull_recline_elimination_age_18_29=[elimination for (age,elimination) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(elimination) is False) and age[0]=='1')]
	nonnull_recline_elimination_age_30_44=[elimination for (age,elimination) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(elimination) is False) and age[0]=='3')]
	nonnull_recline_elimination_age_45_60=[elimination for (age,elimination) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(elimination) is False) and age[0]=='4')]
	nonnull_recline_elimination_age_gt_60=[elimination for (age,elimination) in mixed_values if ((pd.isnull(age) is False) and (pd.isnull(elimination) is False) and age[0]=='>')]
	keys_actual=['Yes','No']
	counter_age_18_29=Counter(nonnull_recline_elimination_age_18_29)
	counter_age_30_44=Counter(nonnull_recline_elimination_age_30_44)
	counter_age_45_60=Counter(nonnull_recline_elimination_age_45_60)
	counter_age_gt_60=Counter(nonnull_recline_elimination_age_gt_60)
	values_age_18_29=[counter_age_18_29[val] for val in keys_actual]
	values_age_30_44=[counter_age_30_44[val] for val in keys_actual]
	values_age_45_60=[counter_age_45_60[val] for val in keys_actual]
	values_age_gt_60=[counter_age_gt_60[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(4)
	bar_width = 0.1
	opacity = 0.8
	# Grouping the plot values
	values1=[values_age_18_29[0],values_age_30_44[0],values_age_45_60[0],values_age_gt_60[0]]
	values2=[values_age_18_29[1],values_age_30_44[1],values_age_45_60[1],values_age_gt_60[1]]

	#Plot 1
	rects1 = plt.bar(index,values1, bar_width,alpha=opacity,color='b',label='Yes')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values2, bar_width,alpha=opacity,color='r',label='No')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Age: 18-29','Age: 30-44','Age: 45-60','Age: > 60',))
	plt.title('Would you eliminate the possibility of Reclining')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_height_and_reclinepreference(data):
	height_values=list((data['How tall are you?']).values)
	reclinepreference_values=list((data['Do you ever recline your seat when you fly?']).values)
	mixed_values=list(zip(height_values,reclinepreference_values))
	nonnull_recline_preference_height_less_than_6=[preference for (height,preference) in mixed_values if ((pd.isnull(height) is False) and (pd.isnull(preference) is False) and height[0]!='6')]
	nonnull_recline_preference_height_more_than_6=[preference for (height,preference) in mixed_values if ((pd.isnull(height) is False) and (pd.isnull(preference) is False) and height[0]=='6')]
	keys_actual=['Once in a while','Usually','Never','Always','About half the time']
	counter_height_less_than_6=Counter(nonnull_recline_preference_height_less_than_6)
	counter_height_more_than_6=Counter(nonnull_recline_preference_height_more_than_6)
	values_height_less_than_6=[counter_height_less_than_6[val] for val in keys_actual]
	values_height_more_than_6=[counter_height_more_than_6[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(5)
	bar_width = 0.1
	opacity = 0.8

	#Plot 1
	rects1 = plt.bar(index, values_height_less_than_6, bar_width,alpha=opacity,color='b',label='Height < 6 feet')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values_height_more_than_6, bar_width,alpha=opacity,color='g',label='Height > 6 feet')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Once in a while','Usually','Never','Always','About half the time'))
	plt.title('Recline Preference grouped by height')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_height_and_reclineobgligation(data):
	height_values=list((data['How tall are you?']).values)
	reclineobligation_values=list((data['Under normal circumstances, does a person who reclines their seat during a flight have any obligation to the person sitting behind them?']).values)
	mixed_values=list(zip(height_values,reclineobligation_values))
	nonnull_recline_obligation_height_less_than_6=[obligation for (height,obligation) in mixed_values if ((pd.isnull(height) is False) and (pd.isnull(obligation) is False) and height[0]!='6')]
	nonnull_recline_obligation_height_more_than_6=[obligation for (height,obligation) in mixed_values if ((pd.isnull(height) is False) and (pd.isnull(obligation) is False) and height[0]=='6')]
	keys_actual=['Yes, they should not recline their chair if the person behind them asks them not to','No, the person on the flight has no obligation to the person behind them']
	counter_height_less_than_6=Counter(nonnull_recline_obligation_height_less_than_6)
	counter_height_more_than_6=Counter(nonnull_recline_obligation_height_more_than_6)
	values_height_less_than_6=[counter_height_less_than_6[val] for val in keys_actual]
	values_height_more_than_6=[counter_height_more_than_6[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(2)
	bar_width = 0.3
	opacity = 0.8

	#Plot 1
	rects1 = plt.bar(index, values_height_less_than_6, bar_width,alpha=opacity,color='b',label='Height < 6 feet')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, values_height_more_than_6, bar_width,alpha=opacity,color='g',label='Height > 6 feet')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Yes, they should listen to the peron behind','No, the need not listen to the person behind'))
	plt.title('Recline- Obligation to person behind grouped by height')
	plt.legend()
	plt.tight_layout()
	plt.show()

def compare_height_and_reclinerudeness(data):
	height_values=list((data['How tall are you?']).values)
	reclinerudeness_values=list((data['Is it rude to recline your seat on a plane?']).values)
	mixed_values=list(zip(height_values,reclinerudeness_values))
	nonnull_recline_rudeness_height_less_than_6=[rudeness for (height,rudeness) in mixed_values if ((pd.isnull(height) is False) and (pd.isnull(rudeness) is False) and height[0]!='6')]
	nonnull_recline_rudeness_height_more_than_6=[rudeness for (height,rudeness) in mixed_values if ((pd.isnull(height) is False) and (pd.isnull(rudeness) is False) and height[0]=='6')]
	keys_actual=['Yes, very rude','Yes, somewhat rude','No, not rude at all']
	counter_height_less_than_6=Counter(nonnull_recline_rudeness_height_less_than_6)
	counter_height_more_than_6=Counter(nonnull_recline_rudeness_height_more_than_6)
	values_height_less_than_6=[counter_height_less_than_6[val] for val in keys_actual]
	values_height_more_than_6=[counter_height_more_than_6[val] for val in keys_actual]
	# Plotting the comparative graph
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(2)
	bar_width = 0.2
	opacity = 0.8

	#Plot 1
	rects1 = plt.bar(index, [values_height_less_than_6[0],values_height_more_than_6[0]], bar_width,alpha=opacity,color='b',label='Yes, very rude')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, [values_height_less_than_6[1],values_height_more_than_6[1]], bar_width,alpha=opacity,color='g',label='Yes, somewhat rude')
	#Plot 3
	rects2 = plt.bar(index+2*bar_width, [values_height_less_than_6[2],values_height_more_than_6[2]], bar_width,alpha=opacity,color='r',label='No, not rude at all')
	# Setting the plot options
	plt.ylabel('Count of Responses')
	plt.xlabel('Type of Response')
	plt.xticks(index + bar_width, ('Height < 6 feet','Height > 6 feet'))
	plt.title('Recline- Is it rude to do it')
	plt.legend()
	plt.tight_layout()
	plt.show()

def main():
	# Establishing path to data which is a directory below/inside
	current_path=os.path.abspath(__file__)
	parent_path=os.path.abspath(os.path.join("."))
	path_to_data=os.path.abspath(os.path.join(parent_path,'Data/flying_etiquette.csv'))
	# Specifying the types
	fy_dtype={
	'RespondentID':str,
	'How often do you travel by plane?':str,
	'Do you ever recline your seat when you fly?':str,
	'How tall are you?':str,
	'Do you have any children under 18?':str,
	'In a row of three seats, who should get to use the two arm rests?':str,
	'In a row of two seats, who should get to use the middle arm rest?':str,
	'Who should have control over the window shade?':str,
	'Is it rude to move to an unsold seat on a plane?':str,
	'Generally speaking, is it rude to say more than a few words tothe stranger sitting next to you on a plane?':str,
	"On a 6 hour flight from NYC to LA, how many times is it acceptable to get up if you're not in an aisle seat?":str,
	'Under normal circumstances, does a person who reclines their seat during a flight have any obligation to the person sitting behind them?':str,
	'Is it rude to recline your seat on a plane?':str,
	'Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?':str,
	'Is it rude to ask someone to switch seats with you in order to be closer to friends?':str,
	'Is it rude to ask someone to switch seats with you in order to be closer to family?':str,
	'Is it rude to wake a passenger up if you are trying to go to the bathroom?':str,
	'Is it rude to wake a passenger up if you are trying to walk around?':str,
	'In general, is it rude to bring a baby on a plane?':str,
	'In general, is it rude to knowingly bring unruly children on a plane?':str,
	"Have you ever used personal electronics during take off or landing in violation of a flight attendant's direction?":str,
	'Have you ever smoked a cigarette in an airplane bathroom when it was against the rules?':str,
	'Gender':str,
	'Age':str,
	'Household Income':str,
	'Education':str,
	'Location (Census Region)':str
	}
	# loading the data
	flying_survey_data=pd.read_csv(path_to_data,dtype=fy_dtype)
	# Calling the functions
	#Comment/Uncomment to activate/suppress function calling
	compare_height_and_reclinepreference(flying_survey_data)
	compare_height_and_reclineobgligation(flying_survey_data)
	compare_height_and_reclinerudeness(flying_survey_data)
	compare_age_and_reclinepreference(flying_survey_data)
	compare_age_and_reclinerudeness(flying_survey_data)
	compare_age_and_reclineelimination(flying_survey_data)
	compare_gender_and_talking(flying_survey_data)
	compare_gender_and_babies(flying_survey_data)
	compare_gender_and_unrulykids(flying_survey_data)
	compare_age_and_bathroom(flying_survey_data)

if __name__=="__main__":
    main()
