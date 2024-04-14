# import requests
# import streamlit as st

# def display_spellcheck_suggestions(query):
#     # Define the base URL for Solr and the core/collection
#     base_url = 'http://localhost:8983/solr/covid-vaccine/spell'
    
#     # Define the spellcheck query parameters
#     params = {
#         'q': query,
#         'spellcheck': 'true',
#         'wt': 'json',  # Specify the response format as JSON
#     }
    
#     # Make an HTTP GET request to the Solr spellcheck endpoint
#     response = requests.get(base_url, params=params)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         data = response.json()
        
#         # Check if there are spellcheck suggestions in the response
#         if 'spellcheck' in data and 'suggestions' in data['spellcheck']:
#             # Access suggestions, usually at index 1, based on Solr's response format
#             suggestions = data['spellcheck']['suggestions']
            
#             # Find suggestions array (it may be located at index 1 in the list of suggestions)
#             if len(suggestions) > 1:
#                 suggestion_list = suggestions[1]['suggestion']
                
#                 # If there are suggestions available, update the query input widget
#                 if suggestion_list:
#                     top_suggestion = suggestion_list[0]['word']
                    
#                     # Display the query input widget with the top suggestion
#                     updated_query = st.text_input('Enter search query:', value=top_suggestion)
#                     return updated_query
#     else:
#         # Log an error message if the HTTP request failed
#         st.error(f"Error: Failed to fetch spellcheck suggestions. Status code: {response.status_code}")
    
#     # If there are no suggestions, return the original query
#     return query

# # Usage in another part of your code:
# search_results = ...  # Your search results data
# query = st.text_input('Enter search query:', value='')  # Initial input query

# updated_query = display_spellcheck_suggestions(query)

# # Now you can use `updated_query` for further processing
