#!/bin/bash
#echo "" > times.txt
for i in {52..100..1}
do
  echo "Testing $i queens"
  python3.6 ex3.py $i >> times.txt
done
