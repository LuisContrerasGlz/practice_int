# Import the pandas library with alias pd
import pandas as pd

# Define a dictionary called personas with three keys: nombre, edad, pais
personas = {
    "nombre": ["Dimas", "Luis", "Fernando"],
    "edad": [23, 24, 25],
    "pais": ["España", "Mexico", "US"]
}

# Create a DataFrame df using the personas dictionary and print it 
df = pd.DataFrame(personas)
print(df)