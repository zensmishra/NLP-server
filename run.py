from flask import Flask, request, json, Response, jsonify
import models.StopListOperations as slo
import models.NLP as nlp

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome to Natural Language Processing for Zendesk'

@app.route('/nlp/', methods = ['POST'])
def api_post_message():
    data = json.loads(json.dumps(request.json))
    print(data)
    message = data["message"]
    resp_data = json.dumps({"keywords" : nlp.get_keyword_confidence(message)})
    return Response(resp_data, status=200, mimetype='application/json')

@app.route('/stoplist/')
def api_get_stoplist():
    data = json.dumps({"data": slo.get_stoplist()})
    return Response(data, status=200, mimetype='application/json')

@app.route('/stoplist/add/<word>', methods = ['POST', 'GET'])
def api_add_stoplist(word):
    data = json.dumps({"data": slo.add_to_stoplist(word)})
    return Response(data, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()