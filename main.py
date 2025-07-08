from flask import Flask, request, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

def get_pytrends():
    lang = request.args.get('lang', 'en-US')
    tz = int(request.args.get('tz', '360'))
    geo = request.args.get('geo', '')
    pytrends = TrendReq(hl=lang, tz=tz)
    return pytrends, geo

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the PyTrends API for Petr Staroba.",
        "documentation": "https://github.com/petaz1987/pytrends-api/blob/main/README.md"
    })

@app.route("/suggestions")
def suggestions():
    keyword = request.args.get('keyword')
    pytrends, _ = get_pytrends()
    data = pytrends.suggestions(keyword)
    return jsonify(data)

@app.route("/related_queries")
def related_queries():
    keyword = request.args.get('keyword')
    pytrends, geo = get_pytrends()
    pytrends.build_payload([keyword], geo=geo)
    data = pytrends.related_queries()
    return jsonify(data)

@app.route("/interest_over_time")
def interest_over_time():
    keyword = request.args.get('keyword')
    pytrends, geo = get_pytrends()
    pytrends.build_payload([keyword], geo=geo)
    data = pytrends.interest_over_time().reset_index().to_dict(orient="records")
    return jsonify(data)

@app.route("/interest_by_region")
def interest_by_region():
    keyword = request.args.get('keyword')
    resolution = request.args.get('resolution', 'COUNTRY')
    pytrends, geo = get_pytrends()
    pytrends.build_payload([keyword], geo=geo)
    data = pytrends.interest_by_region(resolution=resolution).reset_index().to_dict(orient="records")
    return jsonify(data)

@app.route("/trending_searches")
def trending_searches():
    pytrends, geo = get_pytrends()
    pn = geo if geo else 'united_states'
    try:
        data = pytrends.trending_searches(pn=pn).to_dict(orient="records")
    except:
        data = {"error": f"Invalid or unsupported geo: {pn}"}
    return jsonify(data)

@app.route("/top_charts")
def top_charts():
    year = int(request.args.get('year', '2024'))
    hl = request.args.get('lang', 'en-US')
    tz = int(request.args.get('tz', '360'))
    geo = request.args.get('geo', '')
    pytrends = TrendReq(hl=hl, tz=tz)
    try:
        data = pytrends.top_charts(year, hl=hl, tz=tz, geo=geo).to_dict(orient="records")
    except:
        data = {"error": "Could not retrieve top charts. Check parameters."}
    return jsonify(data)
