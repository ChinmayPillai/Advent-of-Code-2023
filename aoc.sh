#!/bin/bash

if [[ -z $1 ]];
then 
    echo "Please specify AOC day"
else
    echo "Day $1"
    mkdir "Day $1"
    cp ./template.py "./Day $1/$1.py"
    touch "./Day $1/$1.txt"
    touch "./Day $1/test.txt"
fi