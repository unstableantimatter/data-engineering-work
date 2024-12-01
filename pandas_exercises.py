# Data frame table summary command syntax
df.column_name.command()

mean	Average of all values in column
std	    Standard deviation
median	Median
max	    Maximum value in column
min	    Minimum value in column
count	Number of values in column
nunique	Number of unique values in column
unique	List of unique values in column

# Checking type of object
print(type(pricey_shoes))

import pandas as pd

# Data Column Aggregate functions
## Using the .reset_index() command will keep the result as a DF not a series and will break the index out to its own column

df.groupby('column1').column2.measurement()
    .reset_index()

# rename df column
teas_counts = teas_counts.rename(columns={"id": "counts"})

# Calculating %-tile of a column set
high_earners = df.groupby('category').wage.apply(lambda x: np.percentile(x, 75)).reset_index()

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

# Aggregate functions grouping by multiple variables.

shoe_counts = orders.groupby(['shoe_type','shoe_color'])['id'].count().reset_index()
print(shoe_counts)

shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id').reset_index()

# Pivot Tables in DFs
df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
         
# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')

# DF Groupby into a Pivot example
user_visits = pd.read_csv('page_visits.csv')

click_source = user_visits.groupby('utm_source').id.count().reset_index()

click_source_by_month = user_visits.groupby(['utm_source','month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(columns='month',
index='utm_source',
values='id').reset_index()

print(click_source_by_month_pivot)

### Reading top 5 rows of a CSV
orders = pd.read_csv('shoefly.csv')
print(orders.head(5))
# Most expensive shoes - max command on  price
most_expensive = orders.price.max()

# number of shoe colors - nunique command on shoe_color
num_colors = orders.shoe_color.nunique()

# Saving / printing out single column from pandas variable ORDERS
emails = orders.email
print(emails)

# Referencing order by first.name column
frances_palmer = orders[orders.first_name == 'Frances']
print(frances_palmer)

# Select sub-group of categories from multiple inputs of shoe_type
comfy_shoes = orders[(orders.shoe_type == 'clogs') |
                    (orders.shoe_type == 'boots') |
                    (orders.shoe_type == 'ballet flats')
                    ]
print(comfy_shoes)


# This command shows us how many users visited the site from different sources in different months.
df.groupby(['month', 'utm_source']).id.count().reset_index()

# This command shows us how many users visited the site from different sources in different months.
df.groupby(['month', 'utm_source']).id.count()\
    .reset_index()\
    .pivot(columns='month', index='utm_source', values='id')


# Reseting a DF index - Restart index at 0..

df.reset_index(inplace=True, drop=True)


# Access data for a specific column values
clinic_df[clinic_df.month = 'May']

# Pandas exercises

# Create df  orders
orders = pd.read_csv('shoefly.csv')

# Lambda function to define source data for the column
source = lambda x: 'animal' if x == 'leather' else 'vegan'

# Creating the shoe_source column, calling source lambda function
orders['shoe_source'] = orders.shoe_material.apply(source)

# Creating  salutation column with lambda function to enter data based on conditional logic and string formatting
orders['salutation'] = orders.apply(lambda row: \
  'Dear Mr. ' + row['last_name']
  if row['gender'] == 'male'
  else 'Dear Ms. ' + row['last_name'],
  axis=1)

print(orders.head())

# DF filtering based on specific entries of multiple columns..
seed_request = inventory.loc[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# Creating new column in_stock that checks if quantity entry of the row is greater than 0.
inventory['in_stock'] = inventory.apply(lambda row: True if row['quantity'] > 0 else False, axis=1)

# Creating new column of total value of in_stock inventory
inventory['total_value'] = inventory.apply(lambda row: row['price'] * row['quantity'], axis=1)

# Creating full description column by combining two other columns string entries - Calling the combine_lambda function

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)


# Pandas Merging dataframes on common columns - pd.merge(table1, table1) - looks for common columns between the 2 DFs and then looks for rows where those columns values are the same. It then combines the matching rows into a single row in a new table.
sales = pd.read_csv('sales.csv')

targets = pd.read_csv('targets.csv')

sales_vs_targets = pd.merge(sales, targets)

# Querying the months  where revenue > targets in the new DF
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# Merging 3 dataframes (sales, targets, men_women) -- and querying the rows on multiple criterion

all_data = sales.merge(targets)\
  .merge(men_women)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

# Merging dataframes, while renaming a column to a common name for the merge to work correctly.
pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))
    
orders_products = pd.merge(
  orders,
  products.rename(columns={'id':'product_id'})
)

# Pandas wont accept 2 columns with the same name, it with either default suffixes, x / y to the column names or you can specify them.
orders_products = pd.merge(
  orders,
  products,
  left_on='product_id',
  right_on='id',
  suffixes=['_orders','_products']
)

# Mismatched IDs on the common columns drop the rows that dont exist (inner merge)

# Outer Joins also work with the added (how='outer) indicator -- this will produce all rows, even if they dont match, but this means NaN cells
store_a_b_outer = pd.merge(store_a, store_b, how='outer')

# Left / right merges -- matching all rows on the first or second dataframe in the function
# basically accomplishes the same thing as an outer join, but narrows in on the individual store based on ordering
store_a_b_left = pd.merge(store_a, store_b, how='left')
store_b_a_left = pd.merge(store_b, store_a, how='left')

# Concatenate two data frames with matching columns names
pd.concat([df1, df2])
menu = pd.concat([bakery, ice_cream])

# Define the column time to be the different between checkout time and visit time - create new column time a product of checkout and visit time.
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time

print(v_to_c.time.mean())


# Multi-DF merge - Specifying type of merge.
all_data = visits.merge(cart, how='left')\
  .merge(checkout, how='left')\
  .merge(purchase, how='left')