from flask import Flask, jsonify, request
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/')
def home():
    return "PyTrends API is running!"

@app.route('/trends', methods=['GET'])
def get_trends():
    kw = request.args.get('keyword', default='AI', type=str)
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([kw], cat=0, timeframe='now 7-d', geo='', gprop='')
    interest = pytrends.interest_over_time()
    if interest.empty:
        return jsonify({'error': 'No data'}), 404
    result = interest[kw].dropna().to_dict()
    return jsonify({'keyword': kw, 'interest': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
