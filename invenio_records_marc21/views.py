# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# Invenio-Records-Marc21 is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Blueprint definitions."""

from __future__ import absolute_import, print_function

from flask import Blueprint

blueprint = Blueprint(
    "invenio_records_marc21",
    __name__,
    template_folder="templates",
    static_folder="static",
)
"""Blueprint used for loading templates and static assets

The sole purpose of this blueprint is to ensure that Invenio can find the
templates and static files located in the folders of the same names next to
this file.
"""


def create_records_blueprint(app):
    """Create records blueprint."""
    ext = app.extensions
    return ext["invenio-records-marc21"].records_resource.as_blueprint(
        "marc21_records_resource"
    )


def create_drafts_blueprint(app):
    """Create drafts blueprint."""
    ext = app.extensions
    return ext["invenio-records-marc21"].drafts_resource.as_blueprint(
        "marc21_draft_resource"
    )
