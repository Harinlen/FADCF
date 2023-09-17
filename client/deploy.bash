#!/bin/bash
create_venv() {
  echo Creating runtime environment...
  CLIENT_PATH=$(dirname $(realpath -s $0))
  cd $CLIENT_PATH
  python -m venv runtime
  source runtime/bin/activate
  
  echo Installing requirements...
  pip install --upgrade pip
  pip install -r requirements.txt
}

create_venv
