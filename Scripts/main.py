# importing pandas library
import pandas as pd

# the path of csv depends on whether you run the script from the same directory or not
# if you run 'python main.py' from the same directory, you can use the following path
# filename = "../CSV_Files/nba.csv"
# if you run 'python Scripts/main.py' from the root directory, you can use the following path
filename = "CSV_Files/nba.csv"
headers = ["Name", "Team", "Number", "Position",
           "Age", "Height", "Weight", "College", "Salary"]

# Read the cvs file
df = pd.read_csv(filename, names=headers)

# To see what the data set looks like, we'll use the head() method.
df.head()
