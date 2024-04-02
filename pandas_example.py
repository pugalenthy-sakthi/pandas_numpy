import pandas as pd
a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])


myds = {
  'data':[1,2],
  'data2':[3,4]
}

df = pd.DataFrame(myds)

rows = df.loc[[0,1]]

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

courses = pd.read_csv('course.csv') 
courses.fillna(0, inplace=True) 

print(courses.all())

courses.to_csv

# df = pd.read_json('data.json')

# print(df['employees'][0]['name'])



