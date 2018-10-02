## Introduction:

This repository does the following: 
1. It is a Natural Language processing server
2. It also creates a dump of the Zendesk data using the API keys
3. Also, houses the NLP client that decodes the underlying message and stores it in the Sentiment table. 


##Steps to run:
#### Run the NLP server:

1. Make sure python3 and pip3 are installed
2. Now, install virtualenv : `pip3 install virtualenv`
3. Create a virtualenvironment named 'venv': `virtualenv venv`
4. Activate the virtual env: `$ source venv/bin/activate`
5. Install the required dependencies: `$ pip install -r requirements.txt`
6. Start the NLP server: `$ python3 run.py`

#### Edit the DB details file:

1. make changes to the connection parameters in `dataimport/initdb.py`

#### Make Zendesk API calls to fetch latest data:

1. Run the file `$ python3 dataimport/zd_api_import.py`
2. This will populate the table `TicketDetails`

#### Run the Sentiment analysis on the tickets data:

1. Run the file `$ python3 dataimport/sentiment_analysis.py`
2. This will populate the table `Sentiment`