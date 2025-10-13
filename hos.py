import streamlit as st
import random
import time

st.title("Hospital Sensor Live Monitoring")
st.write("simulating live sensor data:heart rate,temperature,oxygen level")

def sensor_data_stream():
    while True:
        yield{
            "heart_rate":random.randint(60,100),
            "temperature":round(random.uniform(97.0,100.0),1),
            "oxygen_level":random.randint(90,100)
        }
        time.sleep(1) #simulate real-time delay

#---streamlit UI placeholders---
heart_rate_bar=st.progress(0)
temperaute_bar=st.progress(0)
oxygen_bar=st.progress(0)

heart_rate_text=st.empty()
temperaure_text=st.empty()
oxygen_text=st.empty()

for reading in sensor_data_stream():
    hr=reading["heart_rate"]
    temp=reading["temperature"]
    ox=reading["oxygen_level"]

    #update progress bars(scale%)
    heart_rate_bar.progress(min(hr,100))
    temperaute_bar.progress(int((temp-97)/3*100))
    oxygen_bar.progress(ox)

    #update text display
    heart_rate_text.text("heart rate:{hr}bpm")
    #print(f"heart rate:{hr}bpm")
    temperaure_text.text(f"temperatue:{temp}F")
    #print(f"temperature:{temp}F")
    oxygen_text.text(f"oxygen level:{ox}%")
    #print(f"oxygen level:{ox}%")
