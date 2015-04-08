# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1428362642.20815
=======
_modified_time = 1428466602.63974
>>>>>>> Style-Changes
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/PersonalProduct.html'
_template_uri = 'PersonalProduct.html'
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
        persProducts = context.get('persProducts', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        persProducts = context.get('persProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</body>\n</html>')
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
        persProducts = context.get('persProducts', UNDEFINED)
        __M_writer = context.writer()
<<<<<<< HEAD
        __M_writer('\n<a href="/Store/PersonalProduct.Create">Add item</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Current Price</th>\n        <th>Instruction Form</th>\n        <th>Production time in days</th>\n        <th>Action</th>\n    </tr>\n')
=======
        __M_writer('\r\n<br>\r\n<br>\r\n<a href="/Store/PersonalProduct.Create" class="btn btn-warning">Add item</a>\r\n<br>\r\n<br>\r\n<table class="table table-striped">\r\n    <tr>\r\n        <th>ID</th>\r\n        <th>Name</th>\r\n        <th>Description</th>\r\n        <th>Current Price</th>\r\n        <th>Instruction Form</th>\r\n        <th>Production time in days</th>\r\n        <th>Action</th>\r\n    </tr>\r\n')
>>>>>>> Style-Changes
        for PersonalProduct in persProducts:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.current_price ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.order_form_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.production_time ))
            __M_writer('</td>\n        <td> <a href="/Store/PersonalProduct.edit/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">Edit</a> | <a href="/Store/PersonalProduct.Delete/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">Delete</a>  </td>\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"source_encoding": "ascii", "line_map": {"65": 17, "72": 17, "73": 29, "74": 30, "75": 31, "76": 31, "77": 32, "78": 32, "79": 33, "80": 33, "81": 34, "82": 34, "83": 35, "84": 35, "85": 36, "86": 36, "87": 37, "88": 37, "89": 37, "90": 37, "27": 0, "97": 91, "91": 41, "37": 1, "42": 15, "47": 42, "53": 4, "59": 4}, "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/PersonalProduct.html", "uri": "PersonalProduct.html"}
=======
{"line_map": {"65": 17, "72": 17, "73": 33, "74": 34, "75": 35, "76": 35, "77": 36, "78": 36, "79": 37, "80": 37, "81": 38, "82": 38, "83": 39, "84": 39, "85": 40, "86": 40, "87": 41, "88": 41, "89": 41, "90": 41, "27": 0, "97": 91, "91": 45, "37": 1, "42": 15, "47": 46, "53": 4, "59": 4}, "uri": "PersonalProduct.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/PersonalProduct.html"}
>>>>>>> Style-Changes
__M_END_METADATA
"""
