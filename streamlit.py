import streamlit as st 
import pyogrio

st.title('시군구별 합계출산율')

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

gdf_korea_sido = gpd.read_file('sido.json',engine="pyogrio")


df=pd.read_excel("totalfertilityratenew.xlsx",engine="pyogrio")


korea_5179 = gdf_korea_sido.to_crs(epsg=5179,inplace=False)


gp=df[['합계출산율']]
print(gp.head())

gdf=pd.concat([gdf_korea_sido, gp], axis=1)
print(gdf)

ax = gdf.plot(column='합계출산율', legend=True, cmap="Reds", k=5)
ax.set_axis_off()
plt.show()
