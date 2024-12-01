
#	full_name	gender_age	fractions	probability	grade
#0	Moses Kirckman	M14	69%	89%	11th grade
#1	Timofei Strowan	M18	63%	76%	11th grade

## Change this to this

#	full_name	gender_age	grade	exam	score
#0	Moses Kirckman	M14	11th grade	fractions	69%
#1	Timofei Strowan	M18	11th grade	fractions	63%
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.columns)
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions','probability'], value_name='score', var_name='exam')

print(students)
print(students.head)
print(students.columns)
print(students.exam.value_counts())

##Rename columns after melting
df.columns(["Account", "Account Type", "Amount"])


# Notes on .melt function

#We can use pd.melt() to do this transformation. .melt() takes in a DataFrame, and the columns to unpack:

df = pd.melt(frame=df, id_vars="Account", value_vars=["Checking","Savings"], value_name="Amount", var_name="Account Type")

#The parameters you provide are:
# frame: the DataFrame you want to melt
# id_vars: the column(s) of the old DataFrame to preserve
# value_vars: the column(s) of the old DataFrame that you want to turn into variables
# value_name: what to call the column of the new DataFrame that stores the values
# var_name: what to call the column of the new DataFrame that stores the variables

# Cleaning duplicates from the students data frame
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

duplicates = students.duplicated()
print(students.value_counts)

students = students.drop_duplicates()

duplicates = students.duplicated()
print(students)

# Splitting 2-var column into 2 columns 
# full_name	gender_age	grade	exam	score	gender	age
# 0	Moses Kirckman	M14	11th grade	fractions	69%	M	14

students['gender'] = students.gender_age.str[0:1]
students['age'] = students.gender_age.str[1:]

students = students[['full_name', 'grade', 'exam', 'score', 'gender', 'age']]

# Splitting fullname into first and last name
import codecademylib3_seaborn
import pandas as pd
from students import students

name_split = students['full_name'].str.split(' ')
students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)

print(students.head())
#	full_name	exam	score	gender	age	first_name	last_name
#0	Moses Kirckman	fractions	69%	M	14	Moses	Kirckman


# Changing table data types and formatting
import codecademylib3_seaborn
import pandas as pd
from students import students

# Remove single character from column cells -- % seen below
students.score = students['score'].replace('[\%,]', '', regex=True)

students.score = pd.to_numeric(students.score)

print(students.grade.head())

students.grade = students.grade.str.split('(\d+)', expand=True)[1]

print(students.dtypes)

students.grade = pd.to_numeric(students.grade)
avg_grade = students.grade.mean()

print(avg_grade)

# Filling in nan cells to calculate on columns.
import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)


score_mean = students.score.mean()
print(score_mean)

students = students.fillna(value={"score":0})

score_mean_2 = students.score.mean()
print(score_mean_2)

# Using GLOB to read multiple files into one DF

import glob

files = glob.glob("file*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

df = pd.concat(df_list)

# GLOB Continued
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

print(us_census.head())


### Data Cleaning Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)

gender_split = us_census['GenderPop'].str.split('_')
us_census['Male_Pop'] = gender_split.str.get(0)
us_census['Female_Pop'] = gender_split.str.get(1)

us_census.Male_Pop = us_census['Male_Pop'].replace('[M]', '', regex=True)
us_census.Male_Pop = pd.to_numeric(us_census.Male_Pop)

us_census.Female_Pop = us_census['Female_Pop'].replace('[F]', '', regex=True)
us_census.Female_Pop = pd.to_numeric(us_census.Female_Pop)

# print(us_census.head())
# print(us_census.dtypes)

us_census.Female_Popnan = us_census.TotalPop - us_census.Male_Pop

# print(us_census.Female_Popnan)

us_census.duplicated()
cus_census = us_census.drop_duplicates()

#plt.scatter(cus_census.Female_Pop, us_census.Income)
#plt.show()

cus_census.Hispanic = cus_census['Hispanic'].replace('[\%,]', '', regex=True)
cus_census.Hispanic = pd.to_numeric(cus_census.Hispanic)

cus_census.White = cus_census['White'].replace('[\%,]', '', regex=True)
cus_census.White = pd.to_numeric(cus_census.White)

cus_census.Black = cus_census['Black'].replace('[\%,]', '', regex=True)
cus_census.Black = pd.to_numeric(cus_census.Black)

cus_census.Native = cus_census['Native'].replace('[\%,]', '', regex=True)
cus_census.Native = pd.to_numeric(cus_census.Native)

cus_census.Asian = cus_census['Asian'].replace('[\%,]', '', regex=True)
cus_census.Asian = pd.to_numeric(cus_census.Asian)

cus_census.Pacific = cus_census['Pacific'].replace('[\%,]', '', regex=True)
cus_census.Pacific = pd.to_numeric(cus_census.Pacific)

nanfill = 21
cus_census.Hispanic = cus_census.Hispanic.fillna(nanfill)
cus_census.White = cus_census.White.fillna(nanfill)
cus_census.Black = cus_census.Black.fillna(nanfill)
cus_census.Native = cus_census.Native.fillna(nanfill)
cus_census.Asian = cus_census.Asian.fillna(nanfill)
cus_census.Pacific = cus_census.Pacific.fillna(nanfill)

print(cus_census.head())
print(cus_census.columns)
print(cus_census.dtypes)

plt.hist(cus_census.Hispanic)
plt.show()