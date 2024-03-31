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

# Method 2: Using ZIP

# Define lists containing data for car brands, prices, and availability
marcas = ["Audi", "Mercedes", "BMW", "Kia"]

precio = [2000,12040, 4000, 5000]

disponibilidad = [True, False, True, True]

# Create a DataFrame df2 using the zip() function to combine data from the lists,
# and specifying the column names using the columns parameter

df2 = pd.DataFrame(
    list(zip(marcas, precio, disponibilidad)),
    columns = ["Marca", "precio", "disponibilidad"]

)

print(df2)