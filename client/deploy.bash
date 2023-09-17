#!/bin/bash
create_venv() {
  CLIENT_PATH=$(dirname $(realpath -s $0))
  cd $CLIENT_PATH
  python -m venv runtime
}

create_venv
