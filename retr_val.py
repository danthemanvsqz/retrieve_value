from flask import Flask, request, make_response
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def get_value():
    key = request.args.get('key')
    doc = mongo.db.retr_val.find_one_or_404({"key": key})
    value = doc["value"]
    return make_response(value, 200)
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()



