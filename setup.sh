#!/bin/sh

VENV_PATH="./venv"

! [ -d "$VENV_PATH" ] && python3 -m venv "$VENV_PATH"

chmod +x "$VENV_PATH/bin/activate"
source "$VENV_PATH/bin/activate"
