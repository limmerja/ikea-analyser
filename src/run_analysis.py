# File to run the analysis
import csv

import pandas as pd
import numpy as np

df = pd.read_csv("..\res\ikea.csv", sep=",")
df.head()
