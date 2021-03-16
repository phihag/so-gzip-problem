#/bin/sh
set -e

python gzip_problem.py

wc -c sphere.css
gzip -d <sphere.css.gz | wc -c
