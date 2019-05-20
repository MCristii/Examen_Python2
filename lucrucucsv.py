import pandas as pd
import numpy as np
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    data=pd.read_sql_query("SELECT * from Users", conn)



data["Full Name"] = data['first_name']+" "+data['last_name']
print(data)
print("Mean = ",data['number_of_login'].mean())
print("Standard Deviation = ",data['number_of_login'].std())
writer = pd.ExcelWriter('Users.xlsx')
data.to_excel(writer, sheet_name='bar')
writer.save()