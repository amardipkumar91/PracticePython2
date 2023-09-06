#!/bin/bash

# using nohup to run process in bakcend and save output in some file
nohup python3 $PWD"/gen.py" -r 100 -c name,str >outputString & # first step begin
sleep 5
input=$PWD"/outputString"
while IFS= read -r line
do

 sleep 5
 # using nohup to run process in bakcend and save output in some file
 nohup python3 $PWD"/api.py">api_output & # second step begin
 sleep 5
 filesall=(${PWD}/$line.csv) 
 curl -X POST -F files[]=@${filesall[@]} -s 'http://127.0.0.1:5000/multiple-files-upload' > /dev/null
 
 
 sleep 5
 curl  -X GET -s 'http://127.0.0.1:5000/files/'$line  > /dev/null # third step begin
 
 file1=(${PWD}/$line.csv)
 file2=(${PWD}/new$line.csv)
 diff -w $file1 $file2 && echo "status code--" 0 || echo "status code--" 1

  done < "$input"


