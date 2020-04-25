#!/bin/bash

echo "Running What A Test Pipeline Would Run"

echo "Delete all old test files"
rm .coverage
rm -rf ./test-reports

mkdir -p test-reports/flake8

export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
source ./venv/bin/activate

echo ""
echo "Running Flake8"
flake8 ./pika_worker --output-file=test-reports/flake8/flake8.txt || true
flake8_junit test-reports/flake8/flake8.txt test-reports/flake8/flake8_junit.xml 

echo "Running tests"
PYTHONPATH=`pwd`/src coverage run -m unittest discover
# coverage report

echo "Creating HTML coverage report"
coverage html