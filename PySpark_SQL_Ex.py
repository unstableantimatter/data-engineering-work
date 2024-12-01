# PySpark -- RDD

from pyspark.sql import SparkSession
student_data = [("Chris",1523,0.72,"CA"),
                ("Jake", 1555,0.83,"NY"),
                ("Cody", 1439,0.92,"CA"),
                ("Lisa",1442,0.81,"FL"),
                ("Daniel",1600,0.88,"TX"),
                ("Kelvin",1382,0.99,"FL"),
                ("Nancy",1442,0.74,"TX"),
                ("Pavel",1599,0.82,"NY"),
                ("Josh",1482,0.78,"CA"),
                ("Cynthia",1582,0.94,"CA")]
spark = SparkSession.builder.getOrCreate()
student_rdd = spark.sparkContext.parallelize(student_data)

rdd_transformation = student_rdd.map(lambda x: (x[0], x[1], int(x[2]*100), x[3]))
rdd_transformation.take(5) ## First 5 rows of rdd


sum_gpa = rdd_transformation.map(lambda x: x[2]).reduce(lambda x,y: x + y)
# view the sum
sum_gpa

sum_gpa / rdd_transformation.count()  # get average gpa dividing sum by count


## YOUR SOLUTION HERE ##
rdd_transformation = student_rdd.map(lambda x: (x[0], x[1], x[2]*100, x[3]))
# confirm transformation is correct
rdd_transformation.collect()

## YOUR SOLUTION HERE ##
rdd_filtered = rdd_transformation.filter(lambda x: x[2]>80)
# confirm transformation is correct
rdd_filtered.collect()


# RDD TO DF--- 
# Create an RDD from a list
hrly_views_rdd  = spark.sparkContext.parallelize([
    ["Betty_White" , 288886],
    ["Main_Page", 139564],
    ["New_Year's_Day", 7892],
    ["ABBA", 8154]
])

# Convert RDD to DataFrame
hrly_views_df = hrly_views_rdd\
    .toDF(["article_title", "view_count"])
    
hrly_views_df.show(4, truncate=False)

# Access DataFrame's underlying RDD
hrly_views_df_rdd = hrly_views_df.rdd

# Check object type
print(type(hrly_views_df_rdd)) 
# <class 'pyspark.rdd.RDD'>


# BROADCAST VARIABLES EX -- 
# list of states
states = ['FL', 'NY', 'TX', 'CA', 'NY', 'NY', 'FL', 'TX']
# convert to RDD
states_rdd = spark.sparkContext.parallelize(states)
# dictionary of regions
region = {"NY":"East", "CA":"West", "TX":"South", "FL":"South"}
# broadcast region dictionary to nodes
broadcast_var = spark.sparkContext.broadcast(region)
# map regions to states
result = states_rdd.map(lambda x: broadcast_var.value[x])
# view first four results
result.take(4)
# output : [‘South’, ‘East’, ‘South’, ‘West’]


# Counting coasts in a rdd.
region = ['East', 'East', 'West', 'South', 'West', 'East', 'East', 'West', 'North']
rdd = spark.sparkContext.parallelize(region)

east = spark.sparkContext.accumulator(0)
west = spark.sparkContext.accumulator(0)

def countCoasts(r):
    if 'East' in r: east.add(1)
    elif 'West' in r: west.add(1)
    
rdd.foreach(lambda x: countCoasts(x))
print(east) # output: 4
print(west) # output: 3



# Initializing 
# default setting
rdd_par = spark.sparkContext.parallelize(dataset_name)
# with partition argument of 10
rdd_txt = spark.sparkContext.textFile("file_name.txt", 10)

rdd_txt.getNumPartitions()
# output: 10
spark.stop()

# Accumulators
sat_1500 = spark.sparkContext.accumulator(0)
type(sat_1500)

def count_high_sat_score(r):
    if r[1] > 1500: sat_1500.add(1)
print(count_high_sat_score)

# Transforms
rdd_transformation = student_rdd.map(lambda x: (x[0], x[1], int(x[2]*100), x[3]))
rdd_transformation.collect()

rdd_filtered = rdd_transformation.filter(lambda x: x[2]>80)
rdd_filtered.collect()



# PySpark SQL examples.
hrly_views_df\
    .filter(hrly_views_df.language_code == "kw.m")\
    .show(truncate=False)

hrly_views_df\
    .filter(hrly_views_df.language_code == "kw.m")\
    .select(['language_code', 'article_title', 'hourly_count'])\
    .orderBy('hourly_count', ascending=False)\    
    .show(5, truncate=False)
    
hrly_views_df\
    .select(['language_code', 'hourly_count'])\
    .groupBy('language_code')\
    .sum() \
    .orderBy('sum(hourly_count)', ascending=False)\
    .show(5, truncate=False)
    
# SUM of uniq human visitors grouped by site_type and order from highest to low, by sum visitors
top_visitors_site_type = wiki_uniq_df\
    .select(['site_type','uniq_human_visitors'])\
    .groupBy('site_type')\
    .sum() \
    .orderBy('sum(uniq_human_visitors)', ascending=False)

# show the DataFrame
top_visitors_site_type.show()

# .sql examples w PySpark
query = """SELECT language_code, article_title, hourly_count
    FROM hourly_counts
    WHERE language_code = 'kw.m'
    ORDER BY hourly_count DESC"""

spark.sql(query).show(truncate=False)


from pyspark.sql import SparkSession

# Create a new SparkSession
spark = SparkSession \
    .builder \
    .appName("learning_spark_sql") \
    .getOrCreate()

# Read in Wikipedia Unique Visitors Dataset
wiki_uniq_df = spark.read\
    .option('header', True) \
    .option('delimiter', ',') \
    .option('inferSchema', True) \
    .csv("wiki_uniq_march_2022_w_site_type.csv")

# Create a temporary view with the DataFrame
wiki_uniq_df\
    .createOrReplaceTempView('uniq_visitors_march')

ar_site_visitors_slim_qry = """SELECT domain, uniq_human_visitors FROM uniq_visitors_march WHERE language_code = 'ar'"""
# show the DataFrame
spark.sql(ar_site_visitors_slim_qry).show(truncate=False)

## YOUR SOLUTION HERE ##
site_top_type_qry = """SELECT site_type, SUM(uniq_human_visitors)
    FROM uniq_visitors_march
    GROUP BY site_type
    ORDER BY SUM(uniq_human_visitors) DESC"""

# show the DataFrame
spark.sql(site_top_type_qry).show(truncate=False)

# WRITING data to disc -- Saving DataFrames
hrly_views_df\
    .select(['language_code', 'article_title', 'hourly_count'])\
    .write.csv('cleaned/csv/views_2022_01_01_000000/', mode="overwrite")
    
# Read DataFrame back from disc -- CSVs do not keep schema details
hrly_views_df_restored = spark.read\
    .csv('cleaned/csv/views_2022_01_01_000000/')
hrly_views_df_restored.printSchema()
    
    
##################### USING PARQUET to store data set schemas  #############
##################### Write DataFrame to Parquet ##########################


hrly_views_slim_df
    .write.parquet('cleaned/parquet/views_2022_01_01_000000/', mode="overwrite")

# Read Parquet as DataFrame
hrly_views_df_restored = spark.read\
    .parquet('cleaned/parquet/views_2022_01_01_000000/')

# Check DataFrame's schema
hrly_views_df_restored.printSchema()
