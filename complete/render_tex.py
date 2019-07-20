from templates.tex.render import render as render_tex


def render(cv):
    importance_threshold = 999
    return render_tex(cv, ordered_section_names=None, importance_threshold=importance_threshold)
