import streamlit as st
import datetime
import requests
from query import query_solr


# from display_spellcheck import display_spellcheck_suggestions

def display_individual_tweets(search_results,query):
    num_results = search_results['response']['numFound']
    
    # If the number of search results is less than 3, call the spellcheck function
    if num_results < 15:
        # Call the spellcheck function
        query = display_spellcheck_suggestions(search_results,query)

    for doc in search_results['response']['docs']:
        # Create a container for each tweet
        container = st.container()
        with container:
            # Define the HTML structure for each tweet
            tweet_html = f"""
            <div style="border: 1px solid #e1e8ed; padding: 10px; margin: 10px 0; border-radius: 5px; background-color: #f5f8fa;">
                <img src="https://cdn-icons-png.flaticon.com/512/124/124021.png" alt="Twitter logo" style="position: absolute; top: 23px; right: 10px; width: 23px; height: 23px; border-radius: 50%;">
                <p style="font-size: 18px; font-weight: bold; color: #1da1f2;"top: 20px>
                    <span style="color: #1da1f2;">@</span>{doc.get('username', [''])[0]}
                </p>
                <p style="font-size: 16px; color: #14171a;">
                    {doc.get('Tweet', [''])[0]}
                </p>
                <p style="font-size: 16px; color: #657786;">
                    Date: {format_date(doc.get('Date', [''])[0])}
                </p>
                <p style="font-size: 15px; color: #657786;">
                    <span style="margin-right: 8px;">
                        <img src="https://cdn-icons-png.flaticon.com/128/1388/1388895.png" alt="Retweet Icon" style="width: 15px; height: 20px; vertical-align: middle;"> {doc.get('Retweet_Count', [0])[0]}
                    </span>
                    <span style="margin-right: 8px;">
                        <img src="https://cdn-icons-png.flaticon.com/128/589/589671.png" alt="Reply Icon" style="width: 15px; height: 15px; vertical-align: middle;"> {doc.get('Reply_Count', [0])[0]}
                    </span>
                    <span>
                        <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Favorite Icon" style="width: 15px; height: 15px; vertical-align: middle;"> {doc.get('Favourite_Count', [0])[0]}
                    </span>
                </p>
                <p style="font-size: 14px;">
                    {format_sentiment_tag(doc.get('Sentiment', [''])[0])}
                </p>
                <a href="{doc.get('Tweet_URL', [''])[0]}" style="font-size: 14px; color: #1da1f2; text-decoration: none;" target="_blank">View on Twitter</a>
            </div>
            """
            # Render the HTML content using st.markdown with unsafe_allow_html=True
            st.markdown(tweet_html, unsafe_allow_html=True)

def format_sentiment_tag(sentiment):
    """Return a formatted tag for the given sentiment."""
    if sentiment == "Positive":
        tag_style = "background-color: #4CAF50; color: white;"
        sentiment_text = "Positive"
    elif sentiment == "Negative":
        tag_style = "background-color: #F44336; color: white;"
        sentiment_text = "Negative"
    elif sentiment == "Neutral":
        tag_style = "background-color: #9E9E9E; color: white;"
        sentiment_text = "Neutral"
    else:
        tag_style = "background-color: #9E9E9E; color: white;"  # Default neutral style
        sentiment_text = "Unknown"

    # Return sentiment as a tag with styling
    return f'Sentiment: <span style="padding: 3px 8px; border-radius: 12px; {tag_style}">{sentiment_text}</span>'


def format_date(date_str):
    """Convert date string from ISO format to a more readable format."""
    # Parse the date string using datetime.datetime.fromisoformat method
    # Since the provided date string is in ISO format with a 'Z' at the end, you can remove the 'Z' and use fromisoformat
    date = datetime.datetime.fromisoformat(date_str.replace('Z', ''))

    # Format the date to "1 January 2021, 00:25:26"
    formatted_date = date.strftime('%-d %B %Y, %H:%M:%S')

    return formatted_date



# Function to display spellcheck suggestions as clickable buttons
def display_spellcheck_suggestions(search_results, query):
    # Define the base URL for Solr and the core/collection
    base_url = 'http://localhost:8983/solr/covid-vaccine/spell'
    
    # Define the spellcheck query parameters
    params = {
        'q': query,
        'spellcheck': 'true',
        'wt': 'json',  # Specify the response format as JSON
    }
    # Make an HTTP GET request to the Solr spellcheck endpoint
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if there are spellcheck suggestions in the response
        if 'spellcheck' in data and 'suggestions' in data['spellcheck']:
            # Access the spellcheck suggestions
            suggestions = data['spellcheck']['suggestions']
            
            # Find the suggestion list within the suggestions (it may be at index 1)
            if len(suggestions) > 1:
                suggestion_list = suggestions[1]['suggestion']
                
                # If there are suggestions available, sort them by frequency and get the top 2
                if suggestion_list:
                    # Sort the suggestion list by frequency in descending order
                    suggestion_list.sort(key=lambda x: x['freq'], reverse=True)
                    
                    # Retrieve the top 2 suggestions
                    top_suggestions = suggestion_list[:2]
                    
                    # Print the "Did you mean" question only once
                    st.write("Did you mean:")
                    
                    # Display each top suggestion as a clickable button
                    for suggestion in top_suggestions:
                        suggestion_word = suggestion['word']
                        
                        # Create a button for each suggestion
                        if st.button(f"- {suggestion_word} (Frequency: {suggestion['freq']})"):
                            # If the button is clicked, handle the suggestion click
                            handle_suggestion_click(suggestion_word)
    else:
        # Log an error message if the HTTP request failed
        st.error(f"Error: Failed to fetch spellcheck suggestions. Status code: {response.status_code}")
    
    # Display the original query in the sidebar for reference
    # st.sidebar.write(query)

# Function to handle the suggestion click
def handle_suggestion_click(suggestion_word):
    # Call the query_solr function with the clicked suggestion word
    search_results = query_solr(query_text=suggestion_word)

    # If search results are available, call the display_individual_tweets function
    if search_results:
        display_individual_tweets(search_results, query=suggestion_word)
