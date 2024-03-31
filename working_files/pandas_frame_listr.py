# Creating a dataframe with lists

import pandas as pd

# Method 1: List of lists

# Define the column names for the DataFrame
columns = ["Marca", "precio", "disponibilidad"]

# Define the data for two cars, each represented as a list
cocheA = ["K4", 10000, True]
cocheB = ["K3", 5000, True]

# Create a DataFrame df using the data of the two cars and specifying the column names
df = pd.DataFrame([cocheA, cocheB], columns=columns)
print(df)