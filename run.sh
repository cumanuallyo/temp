#!/bin/bash

for ((i=1;i<=90;i++)); 
do 
   curl checkip.amazonaws.com
   curl -XGET -IL trytravis.tk
   sleep 30s
done