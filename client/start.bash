#!/bin/bash
start_fadcf() {
  source runtime/bin/activate
  python kernel/bootstrap.py
}

start_fadcf
