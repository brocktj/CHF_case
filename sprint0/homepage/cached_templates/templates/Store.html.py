# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423361115.077426
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/Store.html'
_template_uri = 'Store.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n     <p> <a href="/homepage/PersonalProduct/">Manage Customized Products</a></p>\n     <p>   <a href="/homepage/BulkProduct/">Manage Bulk Products</a></p>\n      <p>  <a href="/homepage/IndividualProduct/">Manage Individual products</a></p>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/homepage/PersonalProduct/">Personal Products</a></li>\n                <li><a href="/homepage/BulkProduct/">Bulk Products</a></li>\n                <li><a href="/homepage/IndividualProduct/">Custom Products</a></li>\n                <li><a href="/homepage/WardrobeItem">Wardrobe Items</a></li>\n                <li><a href="">Other Rental Items</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/homepage/templates/Store.html", "line_map": {"64": 19, "36": 1, "70": 19, "41": 18, "58": 12, "27": 0, "76": 70, "46": 32, "52": 12}, "source_encoding": "ascii", "uri": "Store.html"}
__M_END_METADATA
"""
