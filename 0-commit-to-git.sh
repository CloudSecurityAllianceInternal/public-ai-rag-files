#!/bin/bash

rm -rf *~
rm -rf */*~
rm -rf */*/*~

./generate-indexes.py
./make-sitemap-xml.py

git add -A *
git commit -m "updates"
git push
