#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'C:/Users/ASUS/Downloads/IBM PROJECT/hotel_bookings(in).csv'
hotel_data = pd.read_csv(file_path)

# Convert 'arrival_date_month' to a categorical type with the correct order
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                'August', 'September', 'October', 'November', 'December']
hotel_data['arrival_date_month'] = pd.Categorical(hotel_data['arrival_date_month'], categories=months_order, ordered=True)

# 1. Best Time of Year to Book a Hotel Room
# Group by month and count the number of bookings
monthly_bookings = hotel_data.groupby('arrival_date_month').size().reindex(months_order)

# Plotting the number of bookings per month
plt.figure(figsize=(12, 6))
sns.barplot(x=monthly_bookings.index, y=monthly_bookings.values, palette='viridis')
plt.title('Number of Bookings per Month')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# 2. Optimal Length of Stay for the Best Daily Rate
# Calculate the total length of stay (weekend + week nights)
hotel_data['total_stay'] = hotel_data['stays_in_weekend_nights'] + hotel_data['stays_in_week_nights']

# Group by the total length of stay and calculate the average daily rate
length_of_stay_adr = hotel_data.groupby('total_stay')['adr'].mean()

# Plotting the relationship between length of stay and average daily rate
plt.figure(figsize=(12, 6))
sns.lineplot(x=length_of_stay_adr.index, y=length_of_stay_adr.values, marker='o')
plt.title('Average Daily Rate (ADR) by Length of Stay')
plt.xlabel('Total Length of Stay (Nights)')
plt.ylabel('Average Daily Rate (ADR)')
plt.grid(True)
plt.show()

# 3. Factors Contributing to a Higher Number of Special Requests
# Group by the number of special requests and calculate average values for key features
special_requests_analysis = hotel_data.groupby('total_of_special_requests').mean()[['total_stay', 'adults', 'children', 'babies', 'adr']]

# Plotting the relationships
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
features = ['total_stay', 'adults', 'children', 'babies', 'adr']
titles = ['Total Stay (Nights)', 'Number of Adults', 'Number of Children', 'Number of Babies', 'Average Daily Rate (ADR)']

for i, feature in enumerate(features):
    sns.barplot(x=special_requests_analysis.index, y=special_requests_analysis[feature], ax=axes[i//2, i%2])
    axes[i//2, i%2].set_title(f'Average {titles[i]} by Number of Special Requests')
    axes[i//2, i%2].set_xlabel('Number of Special Requests')
    axes[i//2, i%2].set_ylabel(f'Average {titles[i]}')

plt.tight_layout()
plt.show()


# In[ ]:
