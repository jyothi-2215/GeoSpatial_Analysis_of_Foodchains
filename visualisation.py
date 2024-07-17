import pandas as pd
import folium
from folium.plugins import MarkerCluster

m=folium.Map(location=[48.86762,2.3624],tiles='OpenStreetMap',zoom_start=5)

# folium.Marker(location=[48.86762,2.3624],popup='TEXT',icon=folium.Icon(color='blue')).add_to(m)
# folium.Marker(location=[49.86762,1.3624],popup='TEXT',icon=folium.Icon(color='red')).add_to(m) 

df=pd.read_csv('restaurantsGeo.csv')
replace_dict={'BK':'Burger King'}
df=df.replace(replace_dict)
# print(df.head())

markerCluster=MarkerCluster().add_to(m)

for i,row in df.iterrows():
    rest=df.at[i,'restaurant']
    popup=df.at[i,'restaurant'] + '<br>'+ str(df.at[i,'street'])+'<br>'+ str(df.at[i,'zip'])+'<br>'+ str(df.at[i,'city'])
    if rest=='McDonalds':
        color='blue'
    else:
        color='red'
    folium.Marker(location=[df.at[i,'lat'],df.at[i,'lng']],popup=popup,icon=folium.Icon(color=color)).add_to(markerCluster)


m.save('index.html')