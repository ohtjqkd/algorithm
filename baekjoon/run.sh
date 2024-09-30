#!/bin/bash

file=$(find . -name "$2.$1" | head -1)
if [ "go" == $1 ]
then
  cat input.txt | go run $file > output.txt
elif [ $1 == "cpp" ]; then
  g++ $file;
  cat input.txt | ./a.out > output.txt
elif [ "c" == $1 ]; then
  gcc $file;
  cat input.txt | ./a.out > output.txt
elif [ "java" == $1 ]; then
  cat input.txt | java $file > output.txt
elif [ "python" == $1 ]; then
  cat input.txt | python $file > output.txt
else
  echo "Invalid language"
  exit 1;
fi
