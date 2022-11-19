import folium
import streamlit as st
from streamlit_folium import st_folium

def create_map():
    map = folium.Map(
        location=[17.262619, 121.981933], # The reference view when the map is loaded
        zoom_start=8, # A hard-try of zooming in into region 2 / Cagayan Valley
        control_scale=True,
        prefer_canvas=True
    )

    return map

def main():
    st.title("Folium Map")
    map = create_map()
    st_data = st_folium(map, height=500)

main()