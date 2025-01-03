#!/usr/bin/env python
# coding: utf-8

# # Lesson 5: Understanding your Google Cloud Footprint

# In[ ]:


from helper import authenticate
CREDENTIALS, PROJECT_ID = authenticate()


# In[ ]:


from google.cloud import bigquery


# In[ ]:


import pandas as pd


# * A function to export the dataset as pandas data frame.

# In[ ]:


def run_bq_query(sql):

    bq_client = bigquery.Client(
        project = PROJECT_ID,
        credentials = CREDENTIALS)

    job_config = bigquery.QueryJobConfig()
    client_result = bq_client.query(
        sql,
        job_config=job_config)

    job_id = client_result.job_id
    
    df = client_result.result().to_arrow().to_pandas()
    print(f"Finished job_id: {job_id}")
    return df


# * Define the query.

# In[ ]:


query = f"""
SELECT * from `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
LIMIT 5
"""


# In[ ]:


sample_df = run_bq_query(query)


# In[ ]:


# Print the dataframe
sample_df


# In[ ]:


print(sample_df['carbon_footprint_kgCO2e'][0])


# In[ ]:


print(sample_df['service'][0])


# In[ ]:


print(sample_df['carbon_footprint_total_kgCO2e'][0])


# In[ ]:


# Calculate total carbon footprint
sample_df['carbon_footprint_kgCO2e'][0]['scope1'] + \
sample_df['carbon_footprint_kgCO2e'][0]['scope2']['location_based'] +\
sample_df['carbon_footprint_kgCO2e'][0]['scope3']


# * More examples of query.

# In[ ]:


# Select from a specific service, in this case BigQuery
query = f"""
SELECT SUM(carbon_footprint_kgCO2e.scope2.location_based)
FROM `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
WHERE service.description = "BigQuery"
"""


# In[ ]:


df = run_bq_query(query)


# In[ ]:


# Print
df


# In[ ]:


# Select specific column values
query = f"""
SELECT
    usage_month,
    service.description,
    location.location,
    carbon_footprint_total_kgCO2e.location_based
FROM `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
WHERE project.number = 11111
ORDER BY usage_month, service.description
"""


# In[ ]:


df = run_bq_query(query)


# In[ ]:


# Print
df


# In[ ]:


# Total amount of emisions from all projects 
query = f"""
SELECT DISTINCT SUM(carbon_footprint_total_kgCO2e.location_based) as carbon_emissions, project.number
FROM `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
GROUP BY project.number
"""


# In[ ]:


df = run_bq_query(query)


# In[ ]:


# Print
df


# In[ ]:


query = f"""
SELECT DISTINCT SUM(carbon_footprint_total_kgCO2e.location_based)
FROM `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
"""


# In[ ]:


df = run_bq_query(query)


# In[ ]:


# Add the results before to compare the result from the recent query
15854.736771 + 12035.135505 + 520.707209


# In[ ]:


df


# In[ ]:


28410/986


# * Load data into pandas dataframe.

# In[ ]:


query = f"""
SELECT *
FROM `sc-gcp-c5-carbon-emissions.carbonfootprint.sample_data`
"""


# In[ ]:


df = run_bq_query(query)


# In[ ]:


# Print
df

