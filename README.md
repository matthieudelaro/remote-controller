# Remote controller

## Introduction

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
Buttons and associated actions are configurable with the env variable CONTROLLER_CONFIG. For instance:
```bash
CONTROLLER_CONFIG='{"port": 8080, "actions": {"start":"date", "stop":"echo STOPPED"}}' python main.py
```
will serve a controller on port `8080` with two buttons (start and stop), each of them triggering a specific command line (`date` and `echo STOPPED`). Buttons will resize automatically to use fill most of the screen.

![Screenshot](https://user-images.githubusercontent.com/2452725/105953664-d2425480-6073-11eb-8e20-bce53b3d338f.png)

Another example:
```bash
CONTROLLER_CONFIG='{"port": 8080, "actions": {"ON":"bash actions/track_and_record.sh", "OFF":"bash actions/stop.sh", "TOGGLE": "bash actions/toggle_tracking_and_recording.sh"}}' python main.py
```