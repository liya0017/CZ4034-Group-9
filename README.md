# CZ4034-Group-9
For our CZ4034/CZ4021 Information Retrieval Assignment, we are required to build a information retrieval system for sentiment analysis. We have to crawl and obtain a text corpus of a topic based on our own choosing, build a search engine that can perform query and perform sentiment analysis. Our topic of choice is tweets on Covid-19 vaccines, from the year 2021. This repository contains the details and work done by the following team members:

Team Members:
  1. GUO CHENRUI
  2. LIYA D/O FELIX SASI KUMAR
  3. NG ZHENG JIE
  4. WONG WEI KAI
  5. YAP WEE JUN
  6. ERNEST SIM ZI-EN

The Youtube link to a 5min video detailing our project can be found here: https://www.youtube.com/watch?v=QluaayQfO78 and the following are the detailed explanation on Crawling, Indexing, UI and Classification portion of our project.

## Crawling
twitter_crawling.ipynb can be run for crawling. 

To obtain the Twitter authentication token:
1. Log into you Twitter account
2. Right-click anywhere on the page and click on "inspect element"
3. Click on "application"
4. On the side bar you will see columns, in the column that says Storage click the arrow on Cookies then click https://twitter.com 
5. Find the Name “auth_token” and copy that value.

Result CSVs are within the folder


## Indexing

For Apache Solr, our project uses Solr version 8.11.3, the latest version in the 8.x series. The link to the download can be found here https://solr.apache.org/downloads.html 

For installation of Apache Solr, you may refer to the installation guide we created called SOLR Guide.pdf under the Indexing folder where we detailed the necessary steps. More information about the installation of Solr can be found on the main Solr website at https://solr.apache.org/guide/7_0/installing-solr.html. The CSV file solr_tweets.csv found in the same file can be uploaded once Solr has been installed. Replace the original managed-schema file with one provided in the indexing folder to enable the stemming algorithm.



## UI
To run the code:
1. Navigate to the code subfolder within the UI folder.
2. Install streamlit by running `pip install streamlit`
3. Launch the UI by running `streamlit run indexing_ui.py` in your terminal

Query results are in the folder (Query 1-5)

## Classification
Q4&5-Datasets-and-FinetunedSOTA contains the source codes, tweet datasets (csv format), and the finetuned SOTA model. The specific details are as follows:

Jupyter Notebooks=======================================

1 Consolidate Tweets	: 	the notebook used to compile the 4 initial csvs (covid, moderna, pfizer, sinovac) to get tweet_corpus.csv, which was then used to manually doubly label the first 3k tweets (initially only 1.4k singly labelled tweets)

2 Finetune Huggingface	:	the notebook used to perform 1) calculation of interannotator agreement (on 3k doubly labelled tweet_corpus.csv)(yields eval.csv); 2) finetuning huggingface model with 2k train (yields models folder); 3) evaluation of finetuned huggingface model on 1k eval.csv; 4) autolabelling of 5k more tweets for training other ML models (yields train.csv)

3 Label Entire Corpus	: 	the notebook used to label the remaining 42k+ tweets (yields tweet_corpus3.csv)

Note that for Label Entire Corpus.ipynb, you need to download and store the finetuned SOTA model (models folder) in the same subdirectory as the notebook. Please download the zipped file containing it from the gdrive link: https://drive.google.com/drive/folders/1O9eR8s_jGKb-N4PV_iPD1Yfi2SIypYg8?usp=sharing

Tweet Corpuses==========================================

moderna_vaccine		:	raw crawled tweets from moderna vaccine keyword

pfizer_vaccine		:	raw crawled tweets from pfizer vaccine keyword

sinovac_vaccine		:	raw crawled tweets from sinovac vaccine keyword

covid_vaccine		: 	raw crawled tweets from covid vaccine keyword (1.4k tweets singly labelled)

eval			:	the first 1k handlabelled tweets used for evaluation (only first label retained)

train 			: 	7k tweets comprising 2k handlabelled tweets (only first label retained) and 5k autolabelled tweets (by finetuned bertweet model), used for training other ML models

tweet_corpus		:	the entire twitter corpus post manual labelling (only first 3k double handlabelled tweets)

tweet_corpus3 		: 	the final, fully labelled entire twitter corpus (only first label retained for handlabelled tweets)

================================================================================================================================

Q4&5-ML-Techniques folder contains source codes, train.csv, eval.csv, jupyter notebook files, pickle models for classification using ML techniques. To run the jupyter notebook files, read readme.txt and run the jupyter notebook files.
