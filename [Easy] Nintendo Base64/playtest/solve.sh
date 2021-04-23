#!/bin/sh
tr -d '[:space:]' < ../release/output.txt | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
