# -*- coding: utf-8 -*-
"""
    sphinx.domains.ruby
    ~~~~~~~~~~~~~~~~~~~

    The Ruby domain.

    :copyright: Copyright 2010 by SHIBUKAWA Yoshiki
    :license: BSD, see LICENSE for details.
"""

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.compat import Directive
from sphinx.util.docfields import Field, GroupedField, TypedField


class RestObject(ObjectDescription):
    """
    Description of a general Rest object.
    """
    has_arguments = False


class RestResource(RestObject):
    """
    Description of a Rest Reosource
    """
    has_arguments = True


class RestXRefRole(XRefRole):
    pass


class RestDomain(Domain):
    """Rest language domain."""
    name = 'rest'
    label = 'REST'
    object_types = {
        'attribute':   ObjType(l_('attribute'), 'attr'),
        'resource':    ObjType(l_('resource'),  'resc'),
    }

    directives = {
        'resource':    RestResource,
        'attribute':   RestObject,
    }

    roles = {
        'resc':   RestXRefRole(),
    }

    initial_data = {
        'resources': {},  # fullname -> docname, objtype
    }

def setup(app):
    app.add_domain(RestDomain)
