# Python_preprocessing
These are the codes that provide solutions to data preprocessing tasks.

## File: preprocessing_danych_generowanie_dataframe_i_operacje_na_dataframe.py
## Task:
Generate a DataFrame containing student data from two different groups.
The table should contain the following attributes: name, student ID (5 random digits - not necessarily unique),
group number indicated by: I or II, and three columns labeled respectively: Exam I, Exam II, and Project - containing grades in the ⟨2, 5⟩ range.
We assume that each of the groups has 30 students. Then:
Determine how many students achieved the maximum grade;
Determine how many students did not pass Exam II;
Determine the average grades for Exam I in each group;
Determine the correlation between the average grades for Group I and Group II;
Determine the median grade in Group II.
Save the data to a csv file.
Save the data to a JSON file, where the columns are stored in reverse order.

## File: preprocessing_data_generating_dataframe_and_dataframe_operations.py
## Task:
Real financial data contains information about instrument price and technical indicator values.
The decision to buy (BUY or STRONGBUY), sell (SELL or STRONGSELL), or wait (WAIT) is made based on the following indicators,
as well as on the relationship between the indicators and the price.
Load the data into a DataFrame, selecting only 2500 objects from the file;
Remove the columns labeled as SMA14IND and SMA50IND;
For the Close column, calculate the number of missing values. Fix the data by replacing the empty value with the average of two neighboring elements;
In the case of missing data in the SMA14 and SMA50 columns, fix the missing values using any method;
For all remaining attributes, fill in missing values with zeros;
Calculate the correlation between SMA14 and SMA50;
Calculate the correlation between Close and SMA14, as well as between Close and SMA50. Remove the column for which the correlation value was higher;
Provide the number of negative elements for the CCI attribute;
Provide information about the maximum and minimum values for each attribute;
Normalize two selected attributes;
Discretize two selected attributes (divide into 2 and 4 categories, respectively);
On a pie chart, show the distribution of decision values (Decision attribute);
On a line chart, show the variation of the Close attribute;
Save the preprocessed data to a JSON file.

## File: preprocessing_zadanie_na_wygenerowanym_sztucznym_zestawie_danych.py
## Task:
You need to generate an artificial dataset of the same size as the base set. At the same time, you should follow the following assumptions:
the first row of the data should contain random elements in the range ⟨mini, maxi⟩,
where mini is the minimum value of the i-th attribute and maxi is the maximum value of the i-th attribute;
random values in each column cannot exceed the specified range ⟨mini, maxi⟩, for i = 1, 2, ..., k where k is the number of attributes excluding the decision attribute;
changes in values for individual attributes in successive rows must be within the range ⟨prevval − prevval· 1%; prevval + prevval· 1%⟩;
if the result is outside the max (or min) range, the new value should be set to the given range;
after generating the array, you need to calculate the correlation between each column from the first set and the corresponding columns from the second set
(i.e. the correlation between the first columns, the correlation between the second columns, and so on).
