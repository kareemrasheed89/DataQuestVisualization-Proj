#!/usr/bin/env python
# coding: utf-8

# # Lesson 2: Explore Carbon Intensity on the Grid

# * In this classroom, the libraries have been already installed for you.
# * If you would like to run this code on your own machine, make sure to get your Electricity Maps API from their [website](https://www.electricitymaps.com/free-tier-api).

# #### Load the Electricity Maps API for this notebook

# In[ ]:


from helper import load_env
load_env()


# ### Electricity Map's live carbon intensity  endpoint

# * Set location coordinates.
# 
# Remember, you can get the coordinates from [Google Maps](https://www.google.com/maps).

# In[ ]:


# Create a dictionary with the coordinates
coordinates = {
    "lat":34.00906474557528,
    "lon": -118.4984580927553
}


# * Request from the endpoint.

# In[ ]:


# Build the url
url= f"https://api.electricitymap.org/v3/carbon-intensity/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"

# Print the endpoint
print("Endpoint: " + str(url))


# * Prepare the get request.

# In[ ]:


import requests
import helper


# In[ ]:


request = requests.get(
    url,
    headers={"auth-token": helper.load_emaps_api_key()})


# In[ ]:


# This byte format is more compact
request.content
type(request.content)


# > Note: This byte format is more compact and often not human-readable. Additionally, it is not possible to access the fields within this byte data as we would access with key-value pairs in a dictionary. This is why we use json.loads()

# In[ ]:


import json


# In[ ]:


json.loads(request.content)


# * Use the live power breakdown endpoint.

# In[ ]:


# Build the url
url = f"https://api.electricitymap.org/v3/power-breakdown/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"


# In[ ]:


print(url)


# In[ ]:


request = requests.get(
    url,
    headers={"auth-token": helper.load_emaps_api_key()})


# In[ ]:


power_breakdown = json.loads(request.content)

# Print the content
power_breakdown


# * Print some specific values.

# In[ ]:


power_breakdown['renewablePercentage']


# In[ ]:


power_breakdown['fossilFreePercentage']


# In[ ]:


# Power Consumption Breakdown in MegaWatts
power_breakdown['powerConsumptionBreakdown']


# * Do some math to understand better the values above.

# In[ ]:


import numpy as np


# In[ ]:


total_consumption = power_breakdown['powerConsumptionTotal']


# In[ ]:


total_consumption


# In[ ]:


consumption_percent = {
    k: np.round((v/total_consumption) * 100)
    for k,v
    in power_breakdown['powerConsumptionBreakdown'].items()}
consumption_percent


# #### Helper function for the power_stats

# In[ ]:


import helper, requests, json, numpy as np
def power_stats(lat,lon, api_key=helper.load_emaps_api_key()):
    coordinates = { "lat": lat, "lon": lon }

    url_intensity = f"https://api.electricitymap.org/v3/carbon-intensity/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"
    request_intensity = requests.get(url_intensity, headers={"auth-token": api_key})
    intensity = json.loads(request_intensity.content)

    url_breakdown = f"https://api.electricitymap.org/v3/power-breakdown/latest?lat={coordinates['lat']}&lon={coordinates['lon']}"
    request_breakdown = requests.get(url_breakdown, headers={"auth-token": api_key})
    breakdown = json.loads(request_breakdown.content)

    breakdown_abridged = {
        'renewablePercentage': breakdown['renewablePercentage'],
        'fossilFreePercentage': breakdown['fossilFreePercentage'],
        'powerConsumptionBreakdown': breakdown['powerConsumptionBreakdown'],
        'consumption_percent': {
            k: np.round((v/breakdown['powerConsumptionTotal']) * 100) 
            for k, v 
            in breakdown['powerConsumptionBreakdown'].items()
        },
    }
    
    return intensity, breakdown_abridged


# In[ ]:


# Coordinates from a landmark in Taiwan, shown by the instructor in the explanation
intensity, breakdown = power_stats(
    lat=25.0356575108668,
    lon=121.52010809479746)


# In[ ]:


intensity


# In[ ]:


breakdown


# ### Do it yourself! 
# * Get coordinates from a location you want to retrieve the information we got before!
