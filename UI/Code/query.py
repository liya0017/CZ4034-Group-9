
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

#Function to get the solr results based on the query and filter functions

def query_solr(query_text="*", num_rows=100, sentiment=None, start_date=None, end_date=None, sort_by=None):  
    
    # Should be able to use this same url as long as the core name is the same ('covid-vaccine')
    solr_url = "http://localhost:8983/solr/covid-vaccine/select"  
    
    # Construct Solr query parameters
    params = {
        "q": f"Tweet:{query_text}",  
        "rows": num_rows  
    }
    
    # Add sentiment filter if provided
    if sentiment and sentiment != "All":
        params["fq"] = f"Sentiment:{sentiment}"
    
    # Format dates if provided
    formatted_start_date = start_date.strftime("%Y-%m-%dT00:00:00Z") if start_date else None
    formatted_end_date = end_date.strftime("%Y-%m-%dT23:59:59Z") if end_date else None
    
    # Add date filter if provided
    if formatted_start_date and formatted_end_date:
        date_filter = f"Date:[{formatted_start_date} TO {formatted_end_date}]"
        # Combine sentiment and date filters using logical AND
        params["fq"] = f"{params.get('fq', '')} AND {date_filter}" if params.get('fq') else date_filter
    
    # Add sorting parameters to sort by date or retweet count
    if sort_by:
        params["sort"] = sort_by
    
    # get response from SOLR based on parameters passed
    response = requests.get(solr_url, params=params)
    
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        st.error(f"Error querying Solr: {response.status_code}")





