
# coding: utf-8

# In[44]:


import PIL 
import numpy as np
from PIL import Image 
from numpy import asarray
from sklearn.cluster import KMeans
import pandas as pd


# In[45]:


# Load image and convert it into a numpy array 
img = Image.open('mona_lisa.jpg') 
# Using asarray class to convert into numpy array
img_numpy = asarray(img) 
# Check the shape of the numpy array 
print(img_numpy.shape)


# In[46]:


# Create kmeans clusters using scikit learn KMeans 
num_clusters = 256
# Rehspae the numpy array into 2D from 3D
nsamples, nx, ny = img_numpy.shape
numpy_array = img_numpy.reshape((nsamples * nx, ny))
print(numpy_array.shape)


# In[47]:


# Create the clusters 
kmeans = KMeans(n_clusters = num_clusters).fit(numpy_array)
# Get the centroids, labels from the kmeans clusters 
kmeans_centroids = kmeans.cluster_centers_
kmeans_labels = kmeans.labels_ 
# Reduce the colors where each pixel is represented using only 8 bits.
pixel_values = np.array([list(kmeans_centroids[label]) for label in kmeans.labels_])
pixel_values = pixel_values.astype('uint8')
new_colors = pixel_values.reshape(img_numpy.shape)


# In[48]:


# Print the final 256 colors used
final_colors_df = pd.DataFrame(kmeans_centroids, columns=["R", "G", "B"])
final_colors_df


# In[49]:


# Create the new image with the clustered color pixels 
# using fromarray class
new_image = Image.fromarray(new_colors) 
# Type of the image 
print(type(new_image)) 
# Mode of the image
print(new_image.mode) 
# Size the new image 
print(new_image.size)
new_image.save('mona_lisa_compressed.jpeg')
new_image.show()

