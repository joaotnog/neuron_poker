import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# Function to load the data
@st.cache_data(ttl=1)  # Cache the function to improve performance and refresh every 60 seconds
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to plot the data
def plot_data(df):
    fig = go.Figure()
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))
    fig.update_layout(
        title='Real-Time Funds History',
        xaxis_title='Time',
        yaxis_title='Funds',
        legend_title='Player',
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)

# Path to the CSV file
file_path = 'funds_history.csv'

# Streamlit app setup
st.title("Real-Time Funds History Plot")

# Placeholder for the plot
plot_placeholder = st.empty()

# Main loop to update the plot in real-time
while True:
    # Load the data
    df = load_data(file_path)
    
    # Update the plot
    with plot_placeholder.container():
        plot_data(df)
    
    # Refresh the plot every 5 seconds
    time.sleep(1)
