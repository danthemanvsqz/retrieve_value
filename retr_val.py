from flask import Flask, request, make_response
import csv
app = Flask(__name__)

@app.route('/')
def get_value():
    key = request.args.get('key')
    if key:
        with open('data.csv', 'rb') as csvfile:
            data = { row[0] : row[1] for row in csv.reader(csvfile) }
            value = data.get(key)
            if value:
                return make_response(value, 200)
    return make_response('Not Found', 404)
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()
