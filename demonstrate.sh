#/bin/sh
set -e

python gzip_problem.py

md5sum sphere.css
gzip -d <sphere.css.gz | md5sum
