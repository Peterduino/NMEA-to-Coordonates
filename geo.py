import folium
import pynmea2

msg = pynmea2.parse(input("NMEA : "))

x=msg.latitude
y=msg.longitude
map= folium.Map(location=[x,y])
folium.Marker([x,y],popup="Hey !!",icon=folium.Icon(color='red')).add_to(map)
map.save('Carte.html')
