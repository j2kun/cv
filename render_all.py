import json

from industry.render import render as render_resume_html
from complete.render import render as render_complete_html
from academic.render import render as render_academic_html


with open('cv.json', 'r') as infile:
    cv = json.load(infile)

with open('industry/cv.html', 'w') as outfile:
    outfile.write(render_resume_html(cv))

with open('complete/cv.html', 'w') as outfile:
    outfile.write(render_complete_html(cv))

with open('academic/cv.html', 'w') as outfile:
    outfile.write(render_academic_html(cv))
