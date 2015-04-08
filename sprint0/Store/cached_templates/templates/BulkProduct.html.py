# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428362640.278596
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/BulkProduct.html'
_template_uri = 'BulkProduct.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        blkProducts = context.get('blkProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\n                <li><a href="/Store/IndividualProduct/">Individual Products</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        blkProducts = context.get('blkProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<body>\n<a href="/Store/BulkProduct.Create">Add item</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Quantity on hand</th>\n        <th>Current Price</th>\n        <th>Actions</th>\n    </tr>\n')
        for BulkProduct in blkProducts:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( BulkProduct.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.quantity_on_hand ))
            __M_writer('</td>\n        <td>$')
            __M_writer(str( BulkProduct.current_price ))
            __M_writer('</td>\n        <td> <a href="/Store/BulkProduct.edit/')
            __M_writer(str( BulkProduct.id ))
            __M_writer('">Edit</a> | <a href="/Store/BulkProduct.Delete/')
            __M_writer(str( BulkProduct.id ))
            __M_writer('">Delete</a>  </td>\n\n    </tr>\n')
        __M_writer('</table>\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"65": 17, "72": 17, "73": 29, "74": 30, "75": 31, "76": 31, "77": 32, "78": 32, "79": 33, "80": 33, "81": 34, "82": 34, "83": 35, "84": 35, "85": 36, "86": 36, "87": 36, "88": 36, "89": 40, "27": 0, "95": 89, "37": 1, "42": 15, "47": 42, "53": 4, "59": 4}, "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/BulkProduct.html", "uri": "BulkProduct.html"}
__M_END_METADATA
"""
