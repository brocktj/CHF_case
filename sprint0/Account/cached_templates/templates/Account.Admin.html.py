# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425783859.222804
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Account/templates/Account.Admin.html'
_template_uri = 'Account.Admin.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, '/homepage/templates/Adminbase.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<h1>Admin Page</h1>\n<p>Welcome ')
        __M_writer(str( user.first_name ))
        __M_writer(' ')
        __M_writer(str( user.last_name))
        __M_writer(' </p>\n\n<table class="table table-striped">\n    <tr>\n        <td>\n            Username\n        </td>\n        <td>\n            ')
        __M_writer(str( user.username ))
        __M_writer('\n        </td>\n    </tr>\n    <tr>\n        <td>\n            Name\n        </td>\n        <td>\n            ')
        __M_writer(str( user.first_name ))
        __M_writer(' ')
        __M_writer(str( user.last_name ))
        __M_writer('\n        </td>\n    </tr>\n    <tr>\n        <td>\n            Address\n        </td>\n        <td>\n            <p>')
        __M_writer(str( user.address ))
        __M_writer('</p>\n            <p>')
        __M_writer(str( user.city ))
        __M_writer('</p>\n            <p>')
        __M_writer(str( user.state ))
        __M_writer('</p>\n            <p>')
        __M_writer(str( user.zip ))
        __M_writer('</p>\n        </td>\n    </tr>\n\n\n</table>\n<div><a href="/Account/Account.update_password">Change Password</a></div>\n<div><a href="/Account/Account.edit_user_info" class="btn btn-success">Update your information</a></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 35, "65": 35, "66": 36, "67": 36, "68": 37, "69": 37, "70": 38, "71": 38, "77": 71, "27": 0, "35": 1, "40": 46, "46": 9, "53": 9, "54": 11, "55": 11, "56": 11, "57": 11, "58": 19, "59": 19, "60": 27, "61": 27, "62": 27, "63": 27}, "filename": "/Users/brock/sprint0/Account/templates/Account.Admin.html", "uri": "Account.Admin.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
