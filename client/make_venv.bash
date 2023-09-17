#!/bin/bash
CLIENT_PATH=$(dirname $(realpath -s $0))
cd $CLIENT_PATH
python -m venv runtime
