#!/bin/bash

# Explicitly change to app directory
cd /home/pi/Documents/sensor-test || exit

# Activate virtual environment with full path
source /home/pi/Documents/sensor-test/testing-venv/bin/activate

# Verify Python path
echo "Using Python: $(which python3)"
echo "Python path: $(python3 -c 'import sys; print(sys.path)')"

# Run app with visible terminal
lxterminal -e "bash -c 'source /home/pi/Documents/sensor-test/testing-venv/bin/activate && python3 relay_control.py'"
