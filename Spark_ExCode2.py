<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
student_data = [(&#34;Chris&#34;,1523,0.72,&#34;CA&#34;),
                (&#34;Jake&#34;, 1555,0.83,&#34;NY&#34;),
                (&#34;Cody&#34;, 1439,0.92,&#34;CA&#34;),
                (&#34;Lisa&#34;,1442,0.81,&#34;FL&#34;),
                (&#34;Daniel&#34;,1600,0.88,&#34;TX&#34;),
                (&#34;Kelvin&#34;,1382,0.99,&#34;FL&#34;),
                (&#34;Nancy&#34;,1442,0.74,&#34;TX&#34;),
                (&#34;Pavel&#34;,1599,0.82,&#34;NY&#34;),
                (&#34;Josh&#34;,1482,0.78,&#34;CA&#34;),
                (&#34;Cynthia&#34;,1582,0.94,&#34;CA&#34;)]
student_rdd = spark.sparkContext.parallelize(student_data)
rdd_transformation = student_rdd.map(lambda x: (x[0], x[1], int(x[2]*100), x[3]))

states = {&#34;NY&#34;:&#34;New York&#34;, &#34;CA&#34;:&#34;California&#34;, &#34;TX&#34;:&#34;Texas&#34;, &#34;FL&#34;:&#34;Florida&#34;}


# 1. Broadcast the `states` dictionary to Spark Cluster. Save this object as `broadcastStates`.

# In[5]:


## YOUR SOLUTION HERE ##
broadcastStates = spark.sparkContext.broadcast(states)

# confirm type
type(broadcastStates)


# 2. Reference `broadcastStates` to map the two-letter abbreviations to their full names. Save transformed rdd as `rdd_broadcast`.

# In[16]:


## YOUR SOLUTION HERE ##
rdd_broadcast = rdd_transformation.map(lambda x: (x[0],x[1],x[2],broadcastStates.value[x[3]]))

# confirm transformation is correct
rdd_broadcast.collect()


# In[ ]:




<script type="text/javascript" src="https://www.codecademy.com/assets/relay.js"></script></body></html>