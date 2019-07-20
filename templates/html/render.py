from collections import defaultdict
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('templates/html'),
    autoescape=select_autoescape(['html']),
    trim_blocks=True,
    lstrip_blocks=True,
)

template_files = {
    "Education": "education.jinja2",
    "Publications": "publications.jinja2",
    "Preprints": "preprints.jinja2",
    "Talks": "talks.jinja2",
    # "Posters": "posters.jinja2",
    # "Professional Programs": "professional_programs.jinja2",
    "Work Experience": "work_experience.jinja2",
    "Contract Work": "contract_work.jinja2",
    "Service": "service.jinja2",
    "Teaching": "teaching.jinja2",
    "Awards": "awards.jinja2",
    "Other": "generic.jinja2",
}

templates = defaultdict(lambda: "generic.jinja2")
for key, fn in template_files.items():
    templates[key] = fn

template = env.get_template('website_template.jinja2')


def render(cv, ordered_section_names=None, importance_threshold=999):
    with open('templates/html/style.css', 'r') as infile:
        style = infile.read()

    def index_in_ordered_list(section):
        try:
            return ordered_section_names.index(section["section_name"])
        except ValueError:
            return 999999

    if ordered_section_names:
        cv['sections'].sort(key=index_in_ordered_list)

    return template.render(
        templates=templates,
        style=style,
        ordered_section_names=ordered_section_names,
        importance_threshold=importance_threshold,
        **cv
    )
