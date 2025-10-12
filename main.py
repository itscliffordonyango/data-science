import pandas as pd

set_path = "/home/bishop/Y2S2/Data Science/Datasets/penguin.csv"
dataset = pd.read_csv(set_path)

show = dataset.head(10)
# print(show)

random = dataset.sample(10)
# print(random)

size = dataset.shape
# print(size)

# missing values
missing_values = dataset.info()
# print(missing_values)

summary = dataset.describe()
# print(summary)

# including varriables
summary_all = dataset.describe(include="all")
# print(summary_all )

# missing values per varriable 
missing_varriables = dataset.isnull().sum()
# print(missing_varriables)

# delete the unamed varriable 
dataset.drop("Unnamed: 0",axis=1,inplace=True)
# print(delete)
dataset.rename({"sex":"gender"},axis=1,inplace=True)
shows = dataset.head()
print (shows)