from flask import Flask, request, g, render_template, send_file, session, make_response, redirect
import json
import os
from environs import Env
env = Env()
env.read_env()

config_string = env.str("CONTROLLER_CONFIG", default='{"port": 8080, "actions": {"test": "date", "stop": "echo stop"}}')
config = json.loads(config_string)
print(f"config = {json.dumps(config, indent=4)}")

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def endpoint_root():
    return redirect("/controller", code=302)

@app.route('/controller')
def endpoint_controller():
    return serve_controller(request)

def serve_controller(request):
    """Responds to any HTTP request."""
    action_names = config["actions"].keys()
    return render_template('controller.html', data={
        "actions": action_names,
        "style": { "button": {
            "width": "90%",
            "height": f"{90/len(action_names)}%",
        }}
    })

@app.route('/trigger/<path:path>')
def endpoint_trigger(path):
    return react_to_trigger(path)

def react_to_trigger(action_name):
    command = config["actions"][action_name]
    print(f"About to execute command $ {command}")
    os.system(command)
    return f"triggered action {action_name}"

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

def run():
    app.run(host='0.0.0.0', port=config["port"], debug=True)

if __name__ == '__main__':
    run()
