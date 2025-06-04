#!/bin/sh
DEBUG=${DEBUG:-0}
ALLURE=${ALLURE:-1}

rm -rf allure-results allure-report

if [ "$DEBUG" -eq 1 ]; then
  export PWDEBUG=1
fi

python -m pytest --alluredir=allure-results "$@"

if [ "$ALLURE" -eq 1 ]; then
  allure generate allure-results -o allure-report --clean
fi