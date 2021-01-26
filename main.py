from flask import Flask, request, g, render_template, send_file, session, make_response, redirect
import json
from environs import Env
env = Env()
env.read_env()

# config = json.load(env.str("CONTROLLER_CONFIG", default='{"test": "echo test"}'))
config_string = env.str("CONTROLLER_CONFIG", default='{"test": "echo test"}')
config = json.loads(config_string)

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def endpoint_root():
    return redirect("/controller", code=302)

@app.route('/controller')
def endpoint_controller():
    return serve_controller(request)

def serve_controller(request):
    """Responds to any HTTP request."""
    return render_template('controller.html', data={"actions": ["track", "record", "stop"]})

@app.route('/trigger/<path:path>')
def endpoint_trigger(path):
    return react_to_trigger(path)

def react_to_trigger(path):
    print("trigger " + path)
    # print(config[path])
    return "trigger " + path

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) # listen for any origin
# [END gae_python37_app]
