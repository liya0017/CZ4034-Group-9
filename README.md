# CZ4034-Group-9


## Crawling


## Indexing


## UI


## Classification
Q4&5-Datasets-and-FinetunedSOTA contains the source codes, tweet datasets (csv format), and the finetuned SOTA model. The specific details are as follows:

Jupyter Notebooks=======================================

1 Consolidate Tweets	: 	the notebook used to compile the 4 initial csvs (covid, moderna, pfizer, sinovac) to get tweet_corpus.csv, which was then used to manually doubly label the first 3k tweets (initially only 1.4k singly labelled tweets)

2 Finetune Huggingface	:	the notebook used to perform 1) calculation of interannotator agreement (on 3k doubly labelled tweet_corpus.csv)(yields eval.csv); 2) finetuning huggingface model with 2k train (yields models directory); 3) evaluation of finetuned huggingface model on 1k eval.csv; 4) autolabelling of 5k more tweets for training other ML models (yields train.csv)

3 Label Entire Corpus	: 	the notebook used to label the remaining 42k+ tweets (yields tweet_corpus3.csv)

Tweet Corpuses==========================================

moderna_vaccine		:	raw crawled tweets from moderna vaccine keyword

pfizer_vaccine		:	raw crawled tweets from pfizer vaccine keyword

sinovac_vaccine		:	raw crawled tweets from sinovac vaccine keyword

covid_vaccine		: 	raw crawled tweets from covid vaccine keyword (1.4k tweets singly labelled)

eval			:	the first 1k handlabelled tweets used for evaluation (only first label retained)

train 			: 	7k tweets comprising 2k handlabelled tweets (only first label retained) and 5k autolabelled tweets (by finetuned bertweet model), used for training other ML models

tweet_corpus		:	the entire twitter corpus post manual labelling (only first 3k double handlabelled tweets)

tweet_corpus3 		: 	the final, fully labelled entire twitter corpus (only first label retained for handlabelled tweets)

Finetuned BERTweet Model================================

models 			: 	the finetuned BERTweet model trained from the first 2k tweets hand labelled tweets in train.csv. Note that the finetuned model is too large to be uploaded onto this repo, so it can be found via the gdrive link: https://drive.google.com/drive/folders/1O9eR8s_jGKb-N4PV_iPD1Yfi2SIypYg8?usp=sharing

================================================================================================================================

Q4&5-ML-Techniques folder contains source codes, train.csv, eval.csv, jupyter notebook files, pickle models for classification using ML techniques. To run the jupyter notebook files, read readme.txt and run the jupyter notebook files.
