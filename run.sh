#!/bin/sh

gcc -o parser/checkPasswd parser/checkPasswd.c
python server/entrance.py
