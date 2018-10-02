import dataimport.initdb as db
import dataimport.nlp_client as nlpclient

def write_to_sentiment_table(rawtabledata):
    for channel, channel_data in rawtabledata.items():
        for customer, customer_data in channel_data.items():
            for sentiment, sentiment_val in customer_data.items():
                db.insert("Sentiment", [customer, channel, sentiment, sentiment_val])


def truncate_all_sentiment_data():
    db.truncate("Sentiment")

def process_sentiments(channel):
    finalres = {}
    truncate_all_sentiment_data()
    rows = db.select_all_ticketdetails()

    for row in rows:
        result = nlpclient.post_message_to_nlpserver( row[2] + " " + row[3])
        customer = row[0]
        nlpresultdict = result["keywords"]
        if customer in finalres:
            for key, val in nlpresultdict.items():
                if key in finalres[customer]:
                    finalres[customer][key] = finalres[customer][key] + val
                else:
                    finalres[customer][key] = val
        else:
            finalres[customer] = nlpresultdict

    write_to_sentiment_table({channel:finalres})

def main():
    process_sentiments("support-api")

if __name__ == '__main__':
    main()