from templates.html.render import render as render_html


def render(cv):
    importance_threshold = 999
    return render_html(cv, ordered_section_names=None, importance_threshold=importance_threshold)
