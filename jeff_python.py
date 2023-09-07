import pandas as pd
import matplotlib.pyplot as plt

# Import the World Development Indicators data from the provided URL
url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
data = pd.read_csv(url)

# Select the columns you want for the plot
selected_columns = ['Mortality rate, infant (per 1,000 live births)',
                    'GDP per capita (constant 2010 US$)',
                    'Country Name']

# Create a new DataFrame with only the selected columns
selected_data = data[selected_columns]

# Rename the columns for easier access
selected_data.columns = ['Mortality Rate (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']

# Drop rows with missing data (NaN values)
selected_data.dropna(inplace=True)

# Create a scatter plot of Mortality Rate against GDP per capita
plt.figure(figsize=(10, 6))
plt.scatter(selected_data['GDP per capita (constant 2010 US$)'], selected_data['Mortality Rate (per 1,000 live births)'])
plt.title('Mortality Rate vs GDP per Capita')
plt.xlabel('GDP per capita (constant 2010 US$)')
plt.ylabel('Mortality Rate (per 1,000 live births)')
plt.grid(True)

print ("Hello world")

# Show the plot
plt.show()
