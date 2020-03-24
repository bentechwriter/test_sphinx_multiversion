# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Command line:
#       sphinx-multiversion <docs_source> <output_dir>
#   for example:
#       sphinx-multiversion docs docs/build/html
# Note: do not test if <docs_source> must be at root of repo

# Directory structure:
#   docs folder - at repo root contains:
#       css -
#           sidebar widget
#       js -
#           sidebar js
#       _templates -
#           versioning.html - default .html file to generate the version list
#           versions.html - add'l .html file to generate a sidebar versions droplist, because sphinx-rtd-theme >= 0.4.3 does
#               use html_sidebars

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'test_sphinxcontrib_versioning'
copyright = '2020, ben'
author = 'ben'

# The full version, including alpha/beta/rc tags
release = '0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
 #   'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
#    'sphinx.ext.mathjax',
#    'sphinx.ext.viewcode',
#    'sphinxcontrib.httpdomain',
    'sphinx_rtd_theme',
    'sphinx_multiversion',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any paths that contain templates here, relative to this directory.

templates_path = [
    '_templates',
]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# -- Customizations: ---------------------------------------------------------

# Do not use html_sidebars. As of sphinx-rtd-there 0.4.3, rtd does not support html_sidebar.
# Instead, use the versions.html template from:
#   https://holzhaus.github.io/sphinx-multiversion/master/templates.html#templates
#   see, "ReadTheDocs Theme"

html_theme_options = {
    'canonical_url': '',
    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# https://github.com/mixxxdj/manual/blob/manual-2.2.x/source/conf.py

# CSS and JS required for the sidebar widget (note: the sidebar comes from the versions.html template,
#   not from sphinx-rtd-theme. As of sphinx-rtd-theme 0.4.3, rtd does not support html_sidebars
html_css_files = [
    'css/mixxx.css',
    'css/widget-sidebar.css',
]

html_js_files = [
    'js/widget-sidebar.js',
]

# default configuration
# these conf options "should" allow whitelisting branches; "should because not yet tested".
# https://holzhaus.github.io/sphinx-multiversion/master/configuration.html

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False

git_url = 'http://www.github.com'
slack_url = 'http://www.slack.com'