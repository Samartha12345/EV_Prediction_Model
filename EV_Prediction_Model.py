#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


pd.read_csv(r"C:\Users\Dell\Downloads\EV-data\Electric_Vehicle_Population_Data.csv")


# In[4]:


ev = pd.read_csv(r"C:\Users\Dell\Downloads\EV-data\Electric_Vehicle_Population_Data.csv")


# In[11]:


ev.columns


# In[7]:


#Cleaning the data finding out all the null values and handelling all the nulls


# In[6]:


ev.isnull().sum()[ev.isnull().sum()>0]


# In[12]:


ev.County.value_counts()#in this case nulls can be filled with most frequent value


# In[13]:


ev.County.fillna('King',inplace = True)


# In[14]:


ev.City.value_counts()


# In[15]:


ev.City.fillna('Seattle',inplace = True)


# In[37]:


ev.rename(columns={'Postal Code':'Postal_Code','Legislative District':'Legislative_District','Vehicle Location':'Vehicle_Location','Electric Utility':'Electric_Utility','2020 Census Tract':'2020_Census_Tract'},inplace = True)


# In[38]:


list(ev.columns)


# In[39]:


ev.isnull().sum()[ev.isnull().sum()>0]


# In[46]:


ev.Postal_Code.fillna(98052,inplace = True)
ev.Legislative_District.fillna(41,inplace = True)
ev.Vehicle_Location.fillna('POINT (-122.12302 47.67668)',inplace = True)
ev.Electric_Utility.fillna('PUGET SOUND ENERGY INC||CITY OF TACOMA - (WA)',inplace = True)
ev.Census_Tract.fillna(5.303303e+10,inplace = True)


# In[47]:


ev.isnull().sum()[ev.isnull().sum()>0]


# In[42]:


ev.rename(columns={'2020_Census_Tract':'Census_Tract'},inplace = True)


# In[48]:


ev.isnull().sum()


# In[49]:


#Start with analyzing the EV Adoption Over Time by visualizing the number of EVs registered by model year. It will give us an insight into how the EV population has grown over the years:


# In[54]:


ev_adoption_over_yrs = ev['Model Year'].value_counts().sort_index()
ev_adoption_over_yrs


# In[55]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[64]:


plt.figure(figsize=(12,6))
sns.barplot(x = ev_adoption_over_yrs.index,y = ev_adoption_over_yrs.values,palette="viridis")
sns.set_style("whitegrid")
plt.title('EV Adoption Over the years')
plt.xlabel('Years')
plt.ylabel('EV Adoption')
plt.xticks(rotation=45);
plt.tight_layout()


# In[ ]:





# In[81]:


value_counts = ev.Make.value_counts()


# In[86]:


top_ev_makers = value_counts[value_counts > 800]
top_ev_makers


# In[91]:


plt.figure(figsize=(12,6))
sns.barplot(x = top_ev_makers.index,y = top_ev_makers.values,palette = 'viridis')
plt.xticks(rotation=45);
plt.title('TOP EV Makers in USA')
plt.xlabel("EV Makers")
plt.ylabel('Production')


# In[94]:


ev_preferred_type = ev['Electric Vehicle Type'].value_counts()
ev_preferred_type


# In[96]:


plt.figure(figsize=(12,6))
sns.barplot(x = ev_preferred_type.values,y = ev_preferred_type.index,palette = 'rocket')
plt.xticks(rotation=45);
plt.title('EV Preferred Type')
plt.xlabel("EV Adoption")
plt.ylabel('Tyes of Ev')


# In[98]:


top_3_makes = top_ev_makers.head(3).index
top_3_makes


# In[99]:


top_makes_data = ev[ev['Make'].isin(top_3_makes)]
top_makes_data


# In[103]:


ev_model_distribution_top_makes = top_makes_data.groupby(['Make', 'Model']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')
ev_model_distribution_top_makes
top_models = ev_model_distribution_top_makes.head(10)
top_models


# In[107]:


plt.figure(figsize=(12, 10))
sns.barplot(x='Number of Vehicles', y='Model', hue='Make', data=top_models, palette="rocket")
plt.title('Top Models in Top 3 Makes by EV Registrations')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('Model')
plt.legend(title='Make', loc='center right')
plt.tight_layout()
plt.show()


# In[110]:


ev.rename(columns={'Electric Range':'Electric_range'},inplace = True)


# In[117]:


df1 = pd.DataFrame(ev.Electric_range)
df1


# In[135]:


plt.figure(figsize = (12,6))
sns.histplot(ev.Electric_range,bins = 30,kde=True, color='purple')##kde gives PDF of random continous varible
plt.title('Range of EVs')
plt.xlabel("Electric Range of Vehicles")
plt.ylabel('Count of Electric Vehicles')
plt.axvline(ev.Electric_range.mean(), linestyle='--',color='red');##shows mean of electric range of vehciles


# In[136]:


ev.head(2)


# In[143]:


ev_range_over_yrs = ev.groupby('Model Year').Electric_range.mean()
ev_range_over_yrs


# In[151]:


plt.figure(figsize = (12,6))
sns.lineplot(x =ev_range_over_yrs.index,y = ev_range_over_yrs.values,color = 'green',marker = 'o' )
plt.title("EV Range over the years")
plt.xlabel('Model Year')
plt.ylabel("Ev Range")



# In[152]:


from scipy.optimize import curve_fit


# In[154]:


ev_registration_counts = ev['Model Year'].value_counts()
ev_registration_counts


# In[158]:


import numpy as np

# filter the dataset to include years with complete data, assuming 2023 is the last complete year
filtered_years = ev_registration_counts[ev_registration_counts.index <= 2023]

# define a function for exponential growth to fit the data
def exp_growth(x, a, b):
    return a * np.exp(b * x)

# prepare the data for curve fitting
x_data = filtered_years.index - filtered_years.index.min()
y_data = filtered_years.values

# fit the data to the exponential growth function
params, covariance = curve_fit(exp_growth, x_data, y_data)

# use the fitted function to forecast the number of EVs for 2024 and the next five years
forecast_years = np.arange(2024, 2024 + 6) - filtered_years.index.min()
forecasted_values = exp_growth(forecast_years, *params)

# create a dictionary to display the forecasted values for easier interpretation
forecasted_evs = dict(zip(forecast_years + filtered_years.index.min(), forecasted_values))
forecasted_evs


# In[ ]:





# In[160]:


years = np.arange(filtered_years.index.min(), 2029 + 1)
actual_years = filtered_years.index
forecast_years_full = np.arange(2024, 2029 + 1)

# actual and forecasted values
actual_values = filtered_years.values
forecasted_values_full = [forecasted_evs[year] for year in forecast_years_full]

plt.figure(figsize=(12, 8))
plt.plot(actual_years, actual_values, 'bo-', label='Actual Registrations')
plt.plot(forecast_years_full, forecasted_values_full, 'ro--', label='Forecasted Registrations')

plt.title('Current & Estimated EV Market')
plt.xlabel('Year')
plt.ylabel('Number of EV Registrations')
plt.legend()
plt.grid(True)


# In[ ]:




