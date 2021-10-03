#!/bin/bash

for process in $(ps -A | grep python | awk '{print $1;}'); do
    echo "Killing $process"
    kill -9 $process
done

for process in $(ps -A | grep org | awk '{print $1;}'); do
    echo "Killing $process"
    kill -9 $process
done