'''here we wrote some sample ways to read in data and spit ou the pieces hat we want from the database
let's create a function to read in our kind of dataset, then returns as an x and y value that we care about'''


import pandas as pd

def read_my_csv(csvfile):
      data =pd.read_csv(csvfile, sep=' ')
      return data.xaxis, data.yaxis
    
