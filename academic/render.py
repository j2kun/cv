from templates.html.render import render as render_html


def render(cv):
    importance_threshold = 3
    ordered_section_names = [
        "Education",
        "Publications",
        "Preprints",
        "Talks",
        "Posters",
        "Service",
        "Awards",
        "Professional Programs",
        "Teaching",
        "Other",
    ]
    return render_html(cv, ordered_section_names=ordered_section_names, importance_threshold=importance_threshold)
