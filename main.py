from flask import Flask, request, g, render_template, send_file, session, make_response, redirect
import json
import os
from environs import Env
env = Env()
env.read_env()

config_string = env.str("CONTROLLER_CONFIG", default='{"test": "date"}')
config = json.loads(config_string)

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def endpoint_root():
    return redirect("/controller", code=302)

@app.route('/controller')
def endpoint_controller():
    return serve_controller(request)

def serve_controller(request):
    """Responds to any HTTP request."""
    return render_template('controller.html', data={"actions": config.keys()})

@app.route('/trigger/<path:path>')
def endpoint_trigger(path):
    return react_to_trigger(path)

def react_to_trigger(path):
    command = config[path]
    print(f"About to execute command $ {command}")
    os.system(command)
    return "triggered " + path

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) # listen for any origin
