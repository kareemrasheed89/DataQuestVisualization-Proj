#!/usr/bin/env python
# coding: utf-8

# # Lesson 3: Training Models in Low Carbon Regions

# * Import libraries to train a model locally.

# In[ ]:


import numpy as np
from sklearn.datasets import make_blobs
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# * Create a dataset.
# 
# This is an example from the [Advanced Learning Algorithms](https://www.coursera.org/learn/advanced-learning-algorithms) course.

# In[ ]:


classes = 4
m = 100
centers = [[-5, 2], [-2, -2], [1, 2], [5, -2]]
std = 1.0
X_train, y_train = make_blobs(
    n_samples=m, 
    centers=centers, 
    cluster_std=std,
    random_state=30)


# * Create the model.

# In[ ]:


# Create the model
model = Sequential(
    [
        Dense(2, activation = 'relu',   name = "L1"),
        Dense(4, activation = 'linear', name = "L2")
    ]
)


# In[ ]:


model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True),
    optimizer=tf.keras.optimizers.Adam(0.01),
)


# * Train the model.

# In[ ]:


model.fit(
    X_train,y_train,
    epochs=200
)


# ### Running on Google Cloud
# 
# We will use Google Cloud's ML platform, Vertex AI. To run this code on Vertex AI, we first need to:
# 1. Import and initialize the Vertex AI Python SDK
# 2. Write the ML training code to a file
# 3. Configure and submit a training job that runs our training code.

# * Step 1. Initialize Vertex AI.

# In[ ]:


from helper import authenticate
CREDENTIALS, PROJECT_ID = authenticate()


# In[ ]:


from google.cloud import aiplatform


# In[ ]:


aiplatform.init(project=PROJECT_ID,
                credentials=CREDENTIALS,
                )


# * Step 2. Write the ML training code to a file.

# In[ ]:


get_ipython().run_cell_magic('writefile', 'task.py', '\n# import libraries\nimport numpy as np\nfrom sklearn.datasets import make_blobs\nimport tensorflow as tf\nfrom tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\n\n# Create dataset\nclasses = 4\nm = 100\ncenters = [[-5, 2], [-2, -2], [1, 2], [5, -2]]\nstd = 1.0\nX_train, y_train = make_blobs(\n    n_samples=m, \n    centers=centers, \n    cluster_std=std,\n    random_state=30)\n\n# Create the model\nmodel = Sequential(\n    [\n        Dense(2, activation = \'relu\',   name = "L1"),\n        Dense(4, activation = \'linear\', name = "L2")\n    ]\n)\n\nmodel.compile(\n    loss=tf.keras.losses.SparseCategoricalCrossentropy(\n        from_logits=True),\n    optimizer=tf.keras.optimizers.Adam(0.01),\n)\n\n# Train\nmodel.fit(\n    X_train,y_train,\n    epochs=200\n)\n')


# In[ ]:


ls


# In[ ]:


cat task.py


# * Define the Custom Trainin Job.

# > Note: Check here to find more information about [Prebuilt containers for custom training](https://cloud.google.com/vertex-ai/docs/training/pre-built-containers)
# 
# > Note: Check here to find more information about [Carbon free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon)

# In[ ]:


# Choose a location (with carbon free energy available for this example)
REGION = 'us-central1'


# * Create a store bucket.

# In[ ]:


import random
import string


# In[ ]:


def generate_uuid(length: int = 8) -> str:
    return "".join(
        random.choices(
            string.ascii_lowercase + string.digits, 
            k=length))

UUID = generate_uuid()


# In[ ]:


# The unique identifier
UUID


# In[ ]:


from google.cloud import storage


# In[ ]:


storage_client = storage.Client(project = PROJECT_ID,
                                credentials = CREDENTIALS)


# In[ ]:


bucket_name = f'carbon-course-bucket-{UUID}'


# In[ ]:


bucket_name


# In[ ]:


bucket = storage_client.bucket(bucket_name)


# In[ ]:


bucket.create(location=REGION)


# In[ ]:


# Create the CustomTrainingJob
job = aiplatform.CustomTrainingJob(
    display_name='dlai-course-example',
    script_path='task.py',
    container_uri='us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-14.py310:latest',
    staging_bucket=f'gs://{bucket_name}',
    location=REGION,
)


# In[ ]:


model = job.run()


# In[ ]:


# Delete the bucket to clean up resources
bucket.delete(force=True)

