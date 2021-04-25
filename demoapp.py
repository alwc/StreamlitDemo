"""Demo Streamlit app on EC2"""
import streamlit as st
import plotly as py
import plotly.io as pio
from plotly import graph_objects as go


labels = ["People who like streamlit", "People who don't know about streamlit"]
values = [80, 20]


# pull is given as a fraction of the pie radius
fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            textinfo="label+percent",
            insidetextorientation="radial",
            pull=[0, 0, 0.2, 0],  # ,hole = 0.2
        )
    ]
)


fig.update_layout(title_text="Demo streamlit app")


st.plotly_chart(fig, sharing="streamlit")
