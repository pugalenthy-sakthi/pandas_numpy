import time
import pandas as pd

start = time.time()
course_read_using_pandas = pd.read_csv('course.csv')
print('Time taken to read csv file using pandas ',time.time() - start)

start = time.time()

course_read_using_python = open('course.csv','r')
course_read_using_python.read()

print('Time taken to read csv file using Python Open ',time.time() - start)
