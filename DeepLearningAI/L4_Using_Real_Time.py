#!/usr/bin/env python
# coding: utf-8

# # Lesson 4: Using Real-Time Energy Data for Low-Carbon Training

# In[ ]:


# Initialize VertexAI
from helper import authenticate
CREDENTIALS, PROJECT_ID = authenticate()

from google.cloud import aiplatform

aiplatform.init(project=PROJECT_ID,
                credentials=CREDENTIALS,
                )


# #### Load the Electricity Maps API for this notebook

# In[ ]:


import requests
import json


# In[ ]:


from helper import load_env
load_env()


# In[ ]:


from helper import load_emaps_api_key
API_KEY = load_emaps_api_key()


# In[ ]:


# Iowa coordinates for this example
coordinates = {"lat": 41.9216734, "lon": -93.3122705}


# > Note: Check here to find more information about [Carbon free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon)

# In[ ]:


url= f"https://api.electricitymap.org/v3/carbon-intensity/latest?lon={coordinates['lon']}&lat={coordinates['lat']}"


# In[ ]:


request = requests.get(url,
                       headers={"auth-token": API_KEY},)


# In[ ]:


json.loads(request.content)


# In[ ]:


# Dictionary
VERTEX_REGIONS = [
    {"id": "northamerica-northeast1", 
     "name": "Montréal", 
     "lat": 45.5031824, "lon": -73.5698065},
    {"id": "northamerica-northeast2", 
     "name": "Toronto", 
     "lat": 43.6534817, "lon": -79.3839347},
    {"id": "southamerica-east1", 
     "name": "São Paulo", 
     "lat": -23.5506507, "lon": -46.6333824},
    {"id": "us-central1", 
     "name": "Iowa", 
     "lat": 41.9216734, "lon": -93.3122705},
    {"id": "us-east1", 
     "name": "South Carolina", 
     "lat": 33.6874388, "lon": -80.4363743},
    {"id": "us-east4", 
     "name": "Northern Virginia", 
     "lat": -12.548285, "lon": 131.017405},
    {"id": "us-west1", 
     "name": "Oregon", 
     "lat": 43.9792797, "lon": -120.737257},
    {"id": "us-west2", 
     "name": "Los Angeles", 
     "lat": 34.0536909, "lon": -118.242766},
    {"id": "us-west4", 
     "name": "Las Vegas", 
     "lat": 36.1672559, "lon": -115.148516},
    {"id": "asia-east2", 
     "name": "Hong Kong", 
     "lat": 22.2793278, "lon": 114.1628131},
    {"id": "asia-northeast1", 
     "name": "Tokyo", "lat": 35.6828387, "lon": 139.7594549},
    {"id": "asia-northeast3", 
     "name": "Seoul", 
     "lat": 37.5666791, "lon": 126.9782914},
    {"id": "asia-south1", 
     "name": "Mumbai", 
     "lat": 19.0785451, "lon": 72.878176},
    {"id": "asia-southeast1", 
     "name": "Singapore", 
     "lat": 1.357107, "lon": 103.8194992},
    {"id": "asia-southeast2", 
     "name": "Jakarta", 
     "lat": -6.1753942, "lon": 106.827183},
    {"id": "australia-southeast1", 
     "name": "Sydney", 
     "lat": -33.8698439, "lon": 151.2082848},
    {"id": "europe-west1", 
     "name": "Belgium", 
     "lat": 50.6402809, "lon": 4.6667145},
    {"id": "europe-west2", 
     "name": "London", 
     "lat": 51.5073219, "lon": -0.1276474},
    {"id": "europe-west3", 
     "name": "Frankfurt", 
     "lat": 50.1106444, "lon": 8.6820917},
    {"id": "europe-west4", 
     "name": "Netherlands", 
     "lat": 52.2434979, "lon": 5.6343227},
    {"id": "europe-west6", 
     "name": "Zurich", "lat": 47.3744489, "lon": 8.5410422},
]


# In[ ]:


# Returns carbon intensity value of a determinated region
def carbon_intensity(VERTEX_REGIONS, API_KEY, region):

  region_obj = [r for r 
                in VERTEX_REGIONS 
                if region == r["id"]][0]

  url= f"https://api.electricitymap.org/v3/carbon-intensity/latest?lon={region_obj['lon']}&lat={region_obj['lat']}"

  request = requests.get(url,
                       headers={"auth-token": API_KEY},)

  response = json.loads(request.content)

  if "carbonIntensity" not in response.keys():
    raise LookupError(
        f"Carbon intensity data not available "
        f"from Electricity Maps for region {region}."
    )

  return int(response["carbonIntensity"])


# In[ ]:


region = 'asia-northeast3'


# In[ ]:


region_obj = [r for r 
              in VERTEX_REGIONS 
              if region == r["id"]][0]


# In[ ]:


region_obj


# In[ ]:


url= f"https://api.electricitymap.org/v3/carbon-intensity/latest?lon={region_obj['lon']}&lat={region_obj['lat']}"


# In[ ]:


request = requests.get(url,
                      headers={"auth-token": API_KEY},)


# In[ ]:


response = json.loads(request.content)


# In[ ]:


response


# In[ ]:


int(response["carbonIntensity"])


# * Function cleanest will return the region with lowest carbon intensity value

# In[ ]:


def cleanest(VERTEX_REGIONS, API_KEY):

  carbon_intensity_for_regions = []

  for region in VERTEX_REGIONS:
    try:
      carbon_intensity_for_regions.append({
        **region,
        **{"carbon_intensity": carbon_intensity(
            VERTEX_REGIONS, 
            API_KEY, 
            str(region["id"]))}
        })
    except LookupError:  # Skip over errors for individual regions.
        logging.warning(
          f"Could not get carbon intensity data "
            f"for region {region['id']}, so it was skipped."
        )

  return min(carbon_intensity_for_regions, 
             key=lambda x: x["carbon_intensity"])


# In[ ]:


carbon_intensity_for_regions = []


# > **Note**: Each double asterix unpacks each dictionaries, meaning that they take out all the key-value pairs of a dictionary, and then adds the key-value pairs into a new dictionary.

# In[ ]:


for region in VERTEX_REGIONS:
  carbon_intensity_for_regions.append({
      **region,
      **{"carbon_intensity": carbon_intensity(
          VERTEX_REGIONS, 
          API_KEY, 
          str(region["id"]))}
      })


# In[ ]:


print(carbon_intensity_for_regions)


# > **Note**: This syntax, where two dictionaries are unpacked using double asterisks inside curly braces, means: take all the key-value pairs from each dictionary and combine them into a new dictionary.
# 
# For example:
# ```
# d_1 = {'key_1': 1.1}
# d_2 = {'key_2': 2.2}
# 
# d_merged = {**d_1, **d_2} 
# print(d_merged)
# ```
# 

# * Find the lowest region with carbon intensity.

# In[ ]:


min(carbon_intensity_for_regions,
    key=lambda x:x['carbon_intensity'])


# In[ ]:


cleanest_region = cleanest(VERTEX_REGIONS, API_KEY)
print(cleanest_region)


# In[ ]:


# Old carbon intensity region
# old_ca = int(response["carbonIntensity"])
old_ca = 416

# Carbon intensity from the region recently selected
# new_ca = int(cleanest_region["carbonIntensity"])
new_ca = 36

# Compare carbon intensity
old_ca/new_ca


# #### Define the Custom Training Job in Vertex AI.

# In[ ]:


REGION = 'northamerica-northeast1'


# * Set up the bucket name and the storage.

# In[ ]:


# Create a UUID for the bucket name
import random
import string

def generate_uuid(length: int = 8) -> str:
    return "".join(
        random.choices(
            string.ascii_lowercase + string.digits, 
            k=length))


UUID = generate_uuid()


# In[ ]:


bucket_name = f'carbon-course-cleaner-bucket-{UUID}'


# In[ ]:


# Print
bucket_name


# In[ ]:


from google.cloud import storage

storage_client = storage.Client(project = PROJECT_ID,
                                credentials = CREDENTIALS)


# In[ ]:


bucket = storage_client.bucket(bucket_name)


# In[ ]:


bucket.create(location=REGION)


# In[ ]:


# Custom Training Job
job = aiplatform.CustomTrainingJob(
    display_name='dlai-course-example-cleaner',
    script_path='task.py',
    container_uri='us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-14.py310:latest',
    staging_bucket=f'gs://{bucket_name}',
    location=REGION,)

model = job.run()


# In[ ]:


bucket.delete(force=True)


# * Try with 'carbon intensity'

# In[ ]:


url= f"https://api.electricitymap.org/v3/carbon-intensity/history?lon={cleanest_region['lon']}&lat={cleanest_region['lat']}"


# In[ ]:


request = requests.get(url,
                       headers={"auth-token": API_KEY},)


# In[ ]:


response = json.loads(request.content)
response

