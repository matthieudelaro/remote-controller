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
will serve a controller on port `8080` with two buttons (start and stop), each of them triggering a specific command line (`date` and `echo STOPPED`)