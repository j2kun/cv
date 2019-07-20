from templates.tex.render import render as render_tex


def render(cv):
    importance_threshold = 2
    ordered_section_names = [
        "Education",
        "Work Experience",
        "Contract Work",
        "Programming",
        "Publications",
        "Talks",
        "Other",
    ]
    return render_tex(cv, ordered_section_names=ordered_section_names, importance_threshold=importance_threshold)
