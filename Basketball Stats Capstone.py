# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:08:45 2022

@author: vyox
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://hoopshype.com/salaries/players/2021-2022/"

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

salary_table = soup.find('table')

length=len(salary_table.find_all("td"))

player_names=[salary_table.find_all("td")[i].text.strip() for i in range(9,length,4)]

column1=[salary_table.find_all("td")[i].text.strip() for i in range(10,length,4)]

         
df_dict={'player_names':player_names,
          '2019/20':column1}

salary_df=pd.DataFrame(df_dict)
         
salary_df.replace({'\$':''}, regex = True,inplace=True)
salary_df.replace(',','', regex=True, inplace=True)



stats_df=pd.read_csv(r"C:\Users\vyox\Desktop\Capstone\2021-2022totals.csv",encoding="latin-1")

for i in range(len(stats_df["Player"])):
    
    try:

        index=stats_df["Player"][i].index("\\")
        stats_df["Player"][i]=stats_df["Player"][i][0:index]
    except:
        pass
    
complete_df=stats_df.merge(salary_df,how="left", left_on="Player", right_on="player_names")

complete_df.to_csv('2021-2022nba.csv')