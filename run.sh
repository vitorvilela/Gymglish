#!/bin/bash

# Run with: ./run.sh

rm -r __pycache__
rm *~

# Run tests functions
echo "RUNNING TESTS..."
python -m pytest -m long -v
python -m pytest -m short -v
python -m pytest -m phrase -v
python -m pytest -m unicode -v
python -m pytest -m misc -v
python -m pytest -m quote -v

# Run profile function
echo "RUNNING PROFILE..."
python gymglish.py