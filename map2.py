import folium
import pandas
import os


data=pandas.read_csv('resources/Volcanoes.txt')
lat=list(data['LAT'])
lon =list(data['LON'])

elev=list(data['ELEV'])
name=list(data['NAME'])

data1= pandas.read_csv('resources/WATER.csv')
location=list(data1['LOCATION'])
value=list(data1['Value'])

html = """<h4>Volcano information:</h4>
Height: %s m
"""


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[45.45,14.13], zoom_start=6, tiles='Stamen Terrain')


fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker( location=[lt, ln], popup=folium.Popup(iframe), 
    radius = 6, fill_color=color_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name='Population')   

fgp.add_child(folium.GeoJson(data = open('resources/world.json', 'r', encoding='utf-8-sig').readline(), 
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 2000000 
else 'yellow' if 2000000 <= x['properties']['POP2005'] < 5000000 
else 'green' if 5000000 <= x['properties']['POP2005'] < 100000000 
else 'blue' if 100000000 <= x['properties']['POP2005'] < 200000000 else 'pink' }))


fgw = folium.FeatureGroup(name='Value')
for loc, val in zip(location, value):
    iframe = folium.IFrame(html=html % str(val), width=100, height =80)
    fgw.add_child(folium.Marker(location=[]))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save('index.html')
