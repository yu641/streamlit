import streamlit as st 
import pyogrio

pyogrio.core._register_drivers()

st.title('시군구별 합계출산율')

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'

gdf_korea_sido = gpd.read_file('C:/vis/geodata/sido.json')


df=pd.read_excel("C:/vis/totalfertilityratenew.xlsx")


korea_5179 = gdf_korea_sido.to_crs(epsg=5179,inplace=False)


gp=df[['합계출산율']]
print(gp.head())

gdf=pd.concat([gdf_korea_sido, gp], axis=1)
print(gdf)

ax = gdf.plot(column='합계출산율', legend=True, cmap="Reds", k=5)
ax.set_axis_off()
ax.set_title("시군구별 합계출산율")
plt.show()
