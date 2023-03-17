import psycopg2
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# DB Connetion
db_connet = psycopg2.connect(
    user = "bk",
    password= "2562",
    host= "localhost",
    port= 5432,
    database= "MBK_DB"
)

# Data Insertion
X,y = load_iris(return_X_y=True, as_frame=True)
df = pd.concat([X,y], axis=1)