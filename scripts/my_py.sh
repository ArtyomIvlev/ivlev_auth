#!/bin/bash


FILES=$(git diff HEAD --name-only --diff-filter=ACMR | grep -e ".*\.py$")

# replace .py files with .pyi or add .pyi
for pyi_file in $(git diff HEAD --name-only --diff-filter=ACMR | grep -e ".*\.pyi$")
do
    PY_FILE=$(echo $pyi_file | sed 's/.\{1\}$//')
    if grep -q "$PY_FILE" <<< "$FILES";
    then
        FILES="${FILES//$PY_FILE/$pyi_file}"
    else
        FILES="$FILES $pyi_file"
    fi
done

FILE_ARGS=( "$FILES" )  # convert string to array
mypy $FILE_ARGS --config-file mypy.ini --follow-imports=silent
