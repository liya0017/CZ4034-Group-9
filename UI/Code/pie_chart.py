import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# Define colors for each sentiment
SENTIMENT_COLORS = {
    "Positive": "#4CAF50",  # Green for Positive
    "Negative": "#F44336",  # Red for Negative
    "Neutral": "#9E9E9E"   # Gray for Neutral
}

# To generate the pie chart (neutral, positive, or negative)
def generate_pie_chart(search_results):
    st.write('Pie Chart for Sentiments:')
    
    # Get sentiment counts from search results
    sentiment_counts = pd.Series([result['Sentiment'][0] for result in search_results['response']['docs']]).value_counts()
    
    # Get the colors for each sentiment type based on the dictionary
    colors = [SENTIMENT_COLORS[sentiment] for sentiment in sentiment_counts.index]

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Convert the plot to an image
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    
    # Display the image
    st.image(img, use_column_width=True)

# Call your function with the desired search results (replace `search_results` with your actual data)
# generate_pie_chart(search_results)
