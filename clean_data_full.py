#%% import the required python modules
from typing import Type
import pandas as pd

# %% import the dataset
data = pd.read_csv('data/german_data_raw.csv', sep = ";")

# %% get a glimpse of the data
data.head()

# %% show the data types
data.dtypes

# %% rename the 'duration_moonths' column
data = data.rename(columns = {'duration_moonths': 'duration_months'})

# %% show the dtypes (and the columns), again
data.dtypes

# %% Other way of showing information of the columns
data.info()

# %% Show the first 10 values of the 'duration_months' column
data['duration_months'].head()

#%% It is not the right data type
try:
    data['duration_months'].mean()
except TypeError as e:
    print(e)


# %% The dtype is object --> convert it to an integer (whole number)
try:
    data['duration_months'] = data['duration_months'].astype(int)
except ValueError as e:
    print(e)

# %% We get another error --> empty value (NaN). Show the rows (for this column) with NaN
data[data['duration_months'].isna()]

#%% Try to handle than NaN values: replace them with the mean of the column
try:
    data['duration_months'] = data['duration_months'].fillna(data['duration_months'].mean())
except TypeError as e:
    print(e)

#%% This is not possible --> cannot calculate the mean --> first convert to 0
data['duration_months'] = data['duration_months'].fillna(0)

#%% Check if there are still NaN values for this column
data[data['duration_months'].isna()]

#%% Convert to integer, there are no more NaN values
try:
    data['duration_months'] = data['duration_months'].astype(int)
except ValueError as e:
    print(e)

#%% Another error, cannot convert "12" ot integer. Show the column
data.query('duration_months == \'"12"\'')

#%% A nasty data error --> replace the quotes with nothing
data['duration_months'] = data['duration_months'].str.replace('"', '')

#%% Finally we can fill the NA's with zeroes
data['duration_months'] = data['duration_months'].fillna(0)

#%% Convert to integer
data['duration_months'] = data['duration_months'].astype(int)

#%% Replace the zeroes with the mean
data['duration_months'] = data['duration_months'].replace(0, data['duration_months'].mean())

#%% Try it again
data['duration_months'].mean()

# %% That is quite a large mean, let's look to some statistics
data['duration_months'].describe()

#%% let's sort the data frame
data.sort_values(by = 'duration_months', ascending = False)

# %% A very large value blows up the mean, this means we also mis calculated the mean for empty values
print("Good luck with the rest")
