#!/bin/bash
create_venv() {
  echo Creating runtime environment...
  CLIENT_PATH=$(dirname $(realpath -s $0))
  cd $CLIENT_PATH
  python3 -m venv runtime
  source runtime/bin/activate
  
  echo Installing requirements...
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
}

create_venv
