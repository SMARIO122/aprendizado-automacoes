#!/bin/bash
source venv/bin/activate
nohup python app.py > dash.log 2>&1 &
