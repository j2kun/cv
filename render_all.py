import json

from industry.render_html import render as render_industry_html
from complete.render_html import render as render_complete_html
from academic.render_html import render as render_academic_html
from industry.render_tex import render as render_industry_tex
from complete.render_tex import render as render_complete_tex
from academic.render_tex import render as render_academic_tex


with open('cv.json', 'r') as infile:
    cv = json.load(infile)


# html
with open('industry/cv.html', 'w') as outfile:
    outfile.write(render_industry_html(cv))

with open('complete/cv.html', 'w') as outfile:
    outfile.write(render_complete_html(cv))

with open('academic/cv.html', 'w') as outfile:
    outfile.write(render_academic_html(cv))


# tex
with open('industry/cv.tex', 'w') as outfile:
    outfile.write(render_industry_tex(cv))

with open('complete/cv.tex', 'w') as outfile:
    outfile.write(render_complete_tex(cv))

with open('academic/cv.tex', 'w') as outfile:
    outfile.write(render_academic_tex(cv))
