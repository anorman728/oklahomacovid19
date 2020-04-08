#!/bin/bash

# This is meant to be called automatically.  If it's called more than once in a
# single day, the count will be messed up.

# Get latest data.
python3 updatecount.py

# Build graph.
python3 covid19timeline.py
