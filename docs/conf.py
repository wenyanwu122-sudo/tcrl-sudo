import os
from datetime import datetime
from pathlib import Path

CONF_DIR = Path(__file__).resolve().parent

project = "TCRL"
author = "Tencent"
copyright = f"{datetime.now().year}, Tencent"

version = os.environ.get("TCRL_DOC_VERSION", "main")
release = version
lang_code = os.environ.get("TCRL_DOC_LANG", "zh")
language = "zh_CN" if lang_code == "zh" else "en"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["myst.header", "myst.xref_missing", "toc.not_included"]

html_theme = "pydata_sphinx_theme"
html_title = "TCRL 操作手册" if lang_code == "zh" else "TCRL Operation Manual"
html_short_title = "TCRL"
html_static_path = [str(CONF_DIR / "_static")]
html_css_files = ["custom.css"]
html_js_files = ["custom.js"]
templates_path = [str(CONF_DIR / "_templates")]
html_sidebars = {"**": ["sidebar-collapse.html", "sidebar-nav-bs.html"]}
html_last_updated_fmt = "%Y-%m-%d"
html_show_sourcelink = False

html_theme_options = {
    "logo": {"text": "TCRL"},
    "navbar_start": ["navbar-logo"],
    "navbar_center": [],
    "navbar_end": ["search-button", "language-switcher", "version-switcher", "theme-switcher"],
    "show_toc_level": 2,
    "navigation_with_keys": True,
    "collapse_navigation": False,
    "navigation_depth": 4,
    "show_nav_level": 1,
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "switcher": {
        "json_url": "_static/switcher.json",
        "version_match": version,
    },
}

html_context = {
    "tcrl_lang": lang_code,
    "tcrl_other_lang": "en" if lang_code == "zh" else "zh",
    "tcrl_other_lang_label": "English" if lang_code == "zh" else "中文",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
]
