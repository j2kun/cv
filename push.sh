#!/bin/bash

cd academic-cv
onecv-website ../cv.json cv.html 3
onecv-moderncv ../cv.json cv.tex 3
pdflatex cv.tex
cd ..

cd complete 
onecv-website ../cv.json cv.html 3
onecv-moderncv ../cv.json cv.tex 3
pdflatex cv.tex
cd ..

cd research-only 
onecv-website ../cv.json research.html 3
cd ..

cd industry-resume 
onecv-website ../cv.json industry-resume.html 999
onecv-moderncv ../cv.json industry-resume.tex 3
pdflatex industry-resume.tex
cd ..

cd ..
scp -r cv jkun2@math.uic.edu:~/public_html

cd cv
