from templates.html.render import render as render_html


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
    return render_html(cv, ordered_section_names=ordered_section_names, importance_threshold=importance_threshold)
