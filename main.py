from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/get-trends')
def get_trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ['AI automation', 'ERP integration', 'chatGPT']
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='')

    related = pytrends.related_queries()
    keywords = []

    for kw in kw_list:
        if kw in related and 'top' in related[kw]:
            queries = related[kw]['top']
            keywords += list(queries['query'].values[:3])  # top 3 pro každé

    return jsonify({
        "trending_keywords": list(set(keywords))[:10]
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
