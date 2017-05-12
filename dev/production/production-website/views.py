import os

# Import flask dependencies
from flask import Flask, render_template, request, jsonify
from flask import json, send_from_directory
from backend.filterSelection import FilterSelection
from backend.recommend import Recommend

# Define the WSGI application object
app = Flask(__name__, template_folder='templates')

# Configurations
app.config.from_object('config')


@app.route('/')
def homepage():
    return render_template('index.html')


def set_serializer(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


@app.route('/results', methods=['POST'])
def results():
    copied = request.form
    user_pref = copied.to_dict(flat=False)
    print user_pref
    matches = get_recommendation(user_pref)
    print matches
    sample = {'image': 'IMAGE', 'url': 'URL', 'programname': 'PNAME', 'universityname': 'UNAME',
              'blurb': 'BLURB', 'score': 'SCORE', 'outofstate': 'OUTOFSTATE', 'instate': 'INSTATE'}
    sample_res = [sample]
    return render_template('results.html', results=sample_res)
    usnews_val = int(request.args.get('usnews'))
    filters = FilterSelection(usnews=usnews_val)
    common, unique, matches = filters.filter_programs()
    json_str = json.dumps(common, default=set_serializer)
    return jsonify(result=json_str)


def get_recommendation(user_pref):
    rank = str(user_pref['ranking'][0])
    location = user_pref['location[]']
    aoi = user_pref['aoi[]']
    budget = str(user_pref['budget'][0])

    match = Recommend(rank=rank,
                      location=location,
                      aoi=aoi,
                      budget=budget)

    matches = match.recommend_programs()

    return matches


@app.route('/results/assets/<path:path>')
@app.route('/assets/<path:path>')
def send_static(path):
    static_dir = '/home/gradscout/repo/production-website/static'
    return send_from_directory(static_dir, path)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
