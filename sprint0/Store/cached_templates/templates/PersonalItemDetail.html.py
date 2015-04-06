# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425500950.079571
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/PersonalItemDetail.html'
_template_uri = 'PersonalItemDetail.html'
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
        persProduct = context.get('persProduct', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
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
        persProduct = context.get('persProduct', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div>\n     <img src="')
        __M_writer(str( settings.STATIC_URL))
        __M_writer('/Store/media/images/pers')
        __M_writer(str( persProduct.id ))
        __M_writer('.jpg"/>\n        <div>\n     <h1>')
        __M_writer(str( persProduct.name ))
        __M_writer('</h1>\n            </div>\n        <div>\n     <p>')
        __M_writer(str( persProduct.description))
        __M_writer('</p>\n            </div>\n        <div> $')
        __M_writer(str( persProduct.current_price ))
        __M_writer('</div>\n        <a class="btn btn-warning" href="/Store/BulkItemDetail.add_to_cart/')
        __M_writer(str( persProduct.id ))
        __M_writer('">Buy Now</a>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\n                <li><a href="/Store/IndividualProduct/">Custom Products</a></li>\n                <li><a href="/Store/WardrobeItem">Wardrobe Items</a></li>\n                <li><a href="">Other Rental Items</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/Store/templates/PersonalItemDetail.html", "uri": "PersonalItemDetail.html", "line_map": {"64": 14, "65": 14, "66": 14, "67": 16, "68": 16, "69": 19, "38": 1, "71": 21, "72": 21, "73": 22, "74": 22, "43": 25, "86": 26, "80": 26, "48": 39, "92": 86, "54": 12, "27": 0, "70": 19, "62": 12, "63": 14}, "source_encoding": "ascii"}
__M_END_METADATA
"""
