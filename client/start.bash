#!/bin/bash
start_fadcf() {
  source runtime/bin/activate
  python3 kernel/bootstrap.py
}

start_fadcf
