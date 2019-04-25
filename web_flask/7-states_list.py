#!/usr/bin/python3
"""Creates and runs Flask web app"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/states_list')
def render_states():
    return render_template('7-states_list.html', storage=storage.all('State'))

@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
