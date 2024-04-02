import pandas as pd
from numpy import random
from time import time

import csv


courses = pd.read_csv('course.csv')

courses.fillna(random.randint(30,size=(1))[0],inplace=True)
  

new_courses = courses

start = time()

new_courses.to_csv('new_courses.csv')

print(time() - start)

start = time()

columns = courses.columns
columns = columns.to_list()

row_list = []
row_list.append(columns)

for course in courses.values:
  row_list.append(course.tolist())

with open('csv_writer.csv','w',newline='') as file:
  
  writer = csv.writer(file)
  
  writer.writerows(row_list)
  
print(time() - start)
  
