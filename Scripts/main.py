# importing pandas library
import pandas as pd

# the path of cvs file
filename = r"../CSV_Files/nba.csv"
headers = ["Name", "Team", "Number", "Position",
           "Age", "Height", "Weight", "College", "Salary"]

# Read the cvs file
df = pd.read_csv(filename, names=headers)

# To see what the data set looks like, we'll use the head() method.
df.head()
