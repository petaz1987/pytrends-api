from flask import Flask, request, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

def get_pytrends():
    lang = request.args.get('lang', 'cs-CZ')
    tz = int(request.args.get('tz', '120'))
    return TrendReq(hl=lang, tz=tz)

@app.route('/')
def hello():
    return 'Google Trends API is running.'

@app.route('/suggestions')
def suggestions():
    keyword = request.args.get('keyword')
    pytrends = get_pytrends()
    try:
        suggestions = pytrends.suggestions(keyword)
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/related_queries')
def related_queries():
    keyword = request.args.get('keyword')
    pytrends = get_pytrends()
    try:
        pytrends.build_payload([keyword], cat=0, timeframe='now 7-d')
        data = pytrends.related_queries()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/interest_over_time')
def interest_over_time():
    keyword = request.args.get('keyword')
    timeframe = request.args.get('timeframe', 'now 7-d')
    pytrends = get_pytrends()
    try:
        pytrends.build_payload([keyword], cat=0, timeframe=timeframe)
        data = pytrends.interest_over_time()
        return jsonify(data.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/interest_by_region')
def interest_by_region():
    keyword = request.args.get('keyword')
    resolution = request.args.get('resolution', 'COUNTRY')
    pytrends = get_pytrends()
    try:
        pytrends.build_payload([keyword], cat=0, timeframe='now 7-d')
        data = pytrends.interest_by_region(resolution=resolution)
        return jsonify(data.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
