import pandas as pd
import matplotlib.pyplot as plt

# URL to download the CSV file
download_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/"
    "data/master/college-majors/recent-grads.csv"
)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(download_url)

# Check the type of df
print(type(df))  # This will print: <class 'pandas.core.frame.DataFrame'>

# Plotting a simple line graph using matplotlib
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.

plt.show()                           # Show the figure.
