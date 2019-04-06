#!/bin/bash

for filename in `ls graphs/*.csv | sort -V`
do
  echo "***** Processing file $filename *****"
  python3.6 ex3.py $filename
done
