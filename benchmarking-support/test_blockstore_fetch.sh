#!/bin/bash

for TRY in {1..10}
do
    curl http://192.168.0.100:12345/down/index.html?file=onekilo.txt > /dev/null 2>/dev/null
done

