<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.sql import SparkSession

# Create a New SparkSession
spark = SparkSession \
    .builder \
    .appName(&#34;learning_spark_sql&#34;) \
    .getOrCreate()

# Read in Wikipedia Unique Visitors Dataset
wiki_uniq_df = spark.read\
    .option(&#39;header&#39;, True) \
    .option(&#39;delimiter&#39;, &#39;,&#39;) \
    .option(&#39;inferSchema&#39;, True) \
    .csv(&#34;wiki_uniq_march_2022_w_site_type.csv&#34;)


# 1. Filter the DataFrame to sites with `language_code` is `&#34;ar&#34;`.

# In[6]:


## YOUR SOLUTION HERE ##
ar_site_visitors = wiki_uniq_df\
    .filter(wiki_uniq_df.language_code == &#34;ar&#34;)\

# show the DataFrame
ar_site_visitors.show()


# 2. Filter the DataFrame to sites with `language_code` is `&#34;ar&#34;` and keep only the columns `domain` and `uniq_human_visitors`. 

# In[8]:


## YOUR SOLUTION HERE ##
ar_visitors_slim = wiki_uniq_df\
    .filter(wiki_uniq_df.language_code == &#34;ar&#34;)\
    .select([&#39;domain&#39;,&#39;uniq_human_visitors&#39;])

# show the DataFrame
ar_visitors_slim.show()


# 3. Calculate the sum of all `uniq_human_visitors` grouped by `site_type` and ordered from highest to lowest page views.

# In[10]:


## YOUR SOLUTION HERE ##
top_visitors_site_type = wiki_uniq_df\
    .select([&#39;site_type&#39;,&#39;uniq_human_visitors&#39;])\
    .groupBy(&#39;site_type&#39;)\
    .sum() \
    .orderBy(&#39;sum(uniq_human_visitors)&#39;, ascending=False)

# show the DataFrame
top_visitors_site_type.show()


# In[ ]:




<script type="text/javascript" src="https://www.codecademy.com/assets/relay.js"></script></body></html>