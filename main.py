from flask import Flask, request, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)
pytrends = TrendReq(hl='en-US', tz=360)

@app.route("/")
def home():
    return "PyTrends API is running."

@app.route("/interest_over_time")
def interest_over_time():
    kw = request.args.get('keyword')
    pytrends.build_payload([kw])
    data = pytrends.interest_over_time()
    return data.to_json()

@app.route("/interest_by_region")
def interest_by_region():
    kw = request.args.get('keyword')
    pytrends.build_payload([kw])
    data = pytrends.interest_by_region()
    return data.to_json()

@app.route("/related_topics")
def related_topics():
    kw = request.args.get('keyword')
    pytrends.build_payload([kw])
    data = pytrends.related_topics()
    return jsonify(data)

@app.route("/related_queries")
def related_queries():
    kw = request.args.get('keyword')
    pytrends.build_payload([kw])
    data = pytrends.related_queries()
    return jsonify(data)

@app.route("/suggestions")
def suggestions():
    kw = request.args.get('keyword')
    data = pytrends.suggestions(keyword=kw)
    return jsonify(data)

@app.route("/trending_searches")
def trending_searches():
    geo = request.args.get('geo', 'united_states')
    data = pytrends.trending_searches(pn=geo)
    return data.to_json()

@app.route("/top_charts")
def top_charts():
    from datetime import datetime
    year = request.args.get('year', datetime.now().year)
    cid = request.args.get('cid', 'all')
    data = pytrends.top_charts(int(year), cid=cid, hl='en-US', tz=300)
    return data.to_json()

@app.route("/categories")
def categories():
    data = pytrends.categories()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
