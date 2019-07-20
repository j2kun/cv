#!/bin/bash

python render_all.py

cd academic
pdflatex cv.tex
cd ..

cd complete
pdflatex cv.tex
cd ..

cd industry
pdflatex cv.tex
cd ..
