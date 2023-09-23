#!/bin/bash

INPUT_FILE=".git/COMMIT_EDITMSG"

START_LINE=`head -n 1 $INPUT_FILE`

COMMIT_REGEX="(^AF-\d+:.*)"

if [[ $START_LINE =~ $COMMIT_REGEX ]]
then
  echo "Commit message \"$START_LINE\" matches regexp \"$COMMIT_REGEX\""
else
  echo "Commit message \"$START_LINE\" doesn't match regexp \"$COMMIT_REGEX\""
  exit 1
fi
