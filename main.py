import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")
df = pd.read_csv("stress.csv")



st.title("Stress Level Analysis")

#Input
#stage_input = st.selectbox(label="Choose academic stage",options=df["Your Academic Stage"].unique())
stage_input = st.sidebar.selectbox("Choose academic stage",options=df["Your Academic Stage"].unique())

#Timestamp,Your Academic Stage,Peer pressure,Academic pressure from your home,Study Environment,What coping strategy you use as a student?,"Do you have any bad habits like smoking, drinking on a daily basis?",What would you rate the academic  competition in your student life,Rate your academic stress index 

df_filtered = df[df["Your Academic Stage"] == stage_input]

#Avarage numbers
avarage_peer_pressure = round(df_filtered["Peer pressure"].mean(),2)
avarage_academic_pressure = round(df_filtered["Academic pressure from your home"].mean(),2)
avarage_competition = round(df_filtered["What would you rate the academic  competition in your student life"].mean(),2)
avarage_stress = round(df_filtered["Rate your academic stress index "].mean(),2)


kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    metric_peer_pressure = st.metric(label="Peer pressure",value=avarage_peer_pressure)
with kpi_col2:
    metric_academic_pressure = st.metric(label="Academic pressure",value=avarage_academic_pressure)
with kpi_col3:
    metric_avarage_competition = st.metric(label="Avarage competition in student life",value=avarage_competition)
with kpi_col4:
    metric_avarage_stress = st.metric(label="Academic stress",value=avarage_stress)


#Histograns
historigram_peer_pressure = px.histogram(data_frame=df_filtered, x="Peer pressure")
historigram_academic_pressure = px.histogram(data_frame=df_filtered, x="Academic pressure from your home")
historigram_competition = px.histogram(data_frame=df_filtered, x="What would you rate the academic  competition in your student life")
historigram_stress = px.histogram(data_frame=df_filtered, x="Rate your academic stress index ")

kpi_colh1, kpi_colh2, kpi_colh3, kpi_colh4= st.columns(4)

with kpi_colh1:
    st.plotly_chart(historigram_peer_pressure)
with kpi_colh2:    
    st.plotly_chart(historigram_academic_pressure)
with kpi_colh3:    
    st.plotly_chart(historigram_competition)
with kpi_colh4:    
    st.plotly_chart(historigram_stress)

#Academic stress distribution
fig = px.box(df, x="Your Academic Stage", y="Rate your academic stress index ",color="Your Academic Stage")
st.plotly_chart(fig)



#Download
st.download_button("📥 Download filtered data", 
                   df.to_csv(index=False).encode("utf-8"), 
                   "filtered_data.csv", 
                   "text/csv")

st.dataframe(df)