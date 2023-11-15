#!/bin/bash

rm -rf *~
rm -rf */*~
rm -rf */*/*~

./generate-indexes.py

git add -A *
git commit -m "updates"
git push
