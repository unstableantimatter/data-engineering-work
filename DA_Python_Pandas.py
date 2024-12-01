# PANDAS - Data Analysis


import codecademylib3
import pandas as pd

df = pd.read_csv('sample.csv')
print(df)

df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())


df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north

print(type(clinic_north))
print(type(df))


clinic_north_south = df[['clinic_north','clinic_south']]

print(type(clinic_north_south))

# Picking rows from DF.. Headers dont count as a row - index starts at row 0.
march = df.iloc[2]
april_may_june = df.iloc[-3:]

# Selecting Rows
df[df.MyColumnName == desired_column_value]
january = df[df.month == 'January']

march_april = df[(df.month == 'March') |
                  (df.month == 'April')]
				  
# Resetting Indexs
df2 = df.loc[[1, 3, 5]]
df3 = df2.reset_index()
df2.reset_index(inplace = True, drop = True)


##  Final Exercise

orders = pd.read_csv('shoefly.csv')
print(orders)

emails = orders.email

frances_palmer = orders[orders.first_name == 'Frances']
print(frances_palmer)

comfy_shoes = orders[(orders.shoe_type == 'clogs') |
                    (orders.shoe_type == 'boots') |
                    (orders.shoe_type == 'ballet flats')
                    ]
print(comfy_shoes)


# MODIFYING DATAFRAMES WITH LAMBDA FUNCTIONS


# lowercase column of values
import string
df['shoe_type'] = df.shoe_type.apply(string.lower) 

# Creating new column based on other column values
df['in_stock'] = df.shoe_material.apply(lambda x: False if x == 'fabric' else True)

# Creating longer text string based on other column values
df['description'] = df.apply(lambda row: "{} {} bought {} {} {}"\
    .format(row.first_name,
            row.last_name,
            row.shoe_color,
            row.shoe_material,
            row.shoe_type),
    axis=1)
df.head(10)


# DF manipulations - 


# Create new column from product of two other columns
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Custom string values in column
df['Sold in Bulk?'] = ['Yes','Yes','No','No']

# New standard column w same string values
df['Is taxed?'] = "Yes"

# Add column here
df['Margin'] = df.Price - df['Cost to Manufacture'] 

# New column of all lowercase name string values
df['Lowercase Name'] = df.Name.apply(str.lower)

# First and last letter of string lambda function
mylambda = lambda x: x[0] + x[-1]


# Lambda Function syntax
lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

#myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
#These functions do the same thing
#def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
		
# Lambda function to check age
mylambda = lambda x: "Welcome to BattleCity!" if x > 12 else "You must be 13 or older"		

# New DF Column - Last name from full name column
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)


# Calculating Overtime Pay -- Lambda function applied to a DF to create total earn column
total_earned = lambda row:  ((1.5 * row.hourly_wage) * (row.hours_worked - 40)) + (row.hourly_wage * 40) \
  if row.hours_worked > 40 \
  else row.hours_worked * row.hourly_wage  
df['total_earned'] = df.apply(total_earned, axis = 1)

# Renaming Columns of a Dataframe
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

# Use .rename to rename just single columns -- By default it will create a new data frame - Use inplace=True
# Renaming the name column to  movie title -- Using the same data frame with inplace=True 
df.rename(columns={
  'name': 'movie_title'},
  inplace=True)
  
## Shoefly Orders exercises - on Orders Table

source = lambda x: 'animal' if x == 'leather' else 'vegan'
orders['shoe_source'] = orders.shoe_material.apply(source)

orders['salutation'] = orders.apply(lambda row: \
  'Dear Mr. ' + row['last_name']
  if row['gender'] == 'male'
  else 'Dear Ms. ' + row['last_name'],
  axis=1)