pip install folium
inside python in terminal you can ask for help: help(folium.Map)

I. STEP 
create Map object

1. open python in cmd: python 
2. create map object: map = folium.Map(location=[80, -100], zoom_start=6) 
[longitude -90 to 90, latitude -180 to 180]
3. map.save('Map1.html')

When you create .html file, then you can update code with command 'python map1.py' in cmd.


II. STEP 
adding a market to the map
dir(folium) inside python shell in cmd

use: tiles = "Stamen Terrain"

add childre to the map:
map.add_child(folium.Marker(location=[38.58,-99.09], popup='hi I am a marker', icon=folium.Icon(color='green')))

method 2
fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.58,-99.09], popup='hi I am a marker', icon=folium.Icon(color='green')))
map.add_child(fg)

III. STEP
adding multiple markers
for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup='hi I am a marker', icon=folium.Icon(color='green')))

IV. STEP
adding markers from files

pip install pandas

data=pandas.read_csv('resources/Vocanoes.txt')
data
lat=list(data['LAT'])
lon =list(data['LON'])
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup='hi I am a marker', icon=folium.Icon(color='green')))

if you want to see columns of file: data.columns
lat = list(data['LAT'])
lat
data['LAT']

for i, j in zip([1, 2, 3], [4, 5, 6]):
   print(i, 'and', j)

V. STEP
adding text on the map popup window
elev=list(data['ELEV'])
name=list(data['NAME'])

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=[el, nm], icon=folium.Icon(color='green')))

add meter to eltitude:
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+' m', icon=folium.Icon(color='green')))
    fg.add_child(folium.Marker(location=[lt, ln], popup=[(str(el)+' m'), nm], icon=folium.Icon(color='green')))


VI. STEP 
adding new layer - population JSON file

fg.add_child(folium.GeoJson(data = (open('resources\\world.json', 'r', encoding='utf-8-sig').readline())))

folium.GeoJson
GeoJson = a special case of JSON
fg.add_child(folium.GeoJson(data = open('resources\world.json', 'r', encoding='utf-8-sig').readline(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))









