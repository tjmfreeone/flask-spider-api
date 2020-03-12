from flask import Flask,jsonify,request
import importlib
app = Flask(__name__)


@app.route('/api/<apiName>')
def processApiRequest(apiName):
    api = importlib.import_module('Api.'+apiName)
    fm = api.FetchMachine()
    adic = request.args.to_dict()
    res = fm.launch(**adic)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='127.0.0.1')