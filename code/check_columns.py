import pandas as pd
import os

csv_path = r"C:\Users\batis\TA IST 356 Fall25\project-kebatist\data\IMDB Top 250 Movies.csv"

df = pd.read_csv(csv_path)
print("Columns:", df.columns.tolist())