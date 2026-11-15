#!/bin/sh
# build print copies -> PDFs, then the screen (A4 view) copies
cd "$(dirname "$0")" && O=$PWD/out && python3 build.py --print && python3 pdf.py $O/Ch5-revision-booklet.html $O/Ch5-revision-booklet.pdf $O/Ch5-revision-booklet-solutions.html $O/Ch5-revision-booklet-solutions.pdf && python3 build.py
