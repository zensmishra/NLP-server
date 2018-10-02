import requests
import json
import dataimport.initdb as db
import re

url = "https://z3ncompasshelp.zendesk.com/api/v2/tickets.json"

headers = {
    'Authorization': "Basic c21pc2hyYUB6ZW5kZXNrLmNvbS90b2tlbjprTEJNWVZYM25ZdVBpZk5SeUp5ZjNUU2hYV0sxU0M4aUdPQ2hYNHJh",
    'Cache-Control': "no-cache"
    }

def list_to_csv(list):
    if len(list)==0:
        return "-"
    valstr = ""
    for i, val in enumerate(list):
        if i == len(list)-1:
            valstr = valstr + str(val)
        else:
            valstr = valstr + str(val)+ ","

    print(valstr)
    return valstr

def truncate_all_ticket_details():
    db.truncate("TicketDetails")

def import_data_from_zd_api():
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    for i,data in enumerate(data["tickets"]):
        id = data["id"]
        problem = re.sub(r'([^\s\w]|_)+', "", data["subject"])
        details = re.sub(r'([^\s\w]|_)+', "", data["description"])
        tags = list_to_csv(data["tags"])
        customer = data["organization_id"]
        channel = "support-api"
        highlights = ""
        created_at = data["created_at"]

        insertdata = [id, customer,channel,details,highlights,problem,tags,created_at]
        db.insert("TicketDetails", insertdata)

    print("Data has been written to TicketDetails")


def main():
    truncate_all_ticket_details()
    import_data_from_zd_api()

if __name__ == '__main__':
    main()