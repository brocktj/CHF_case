# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428467058.909304
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\homepage\\templates/Users.html'
_template_uri = 'Users.html'
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
        users = context.get('users', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head lang="en">\r\n    <meta charset="UTF-8">\r\n    <title></title>\r\n</head>\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n    <div id="left side" class="col-md-2">\r\n        <nav>\r\n            <ul class="nav nav-pills nav-stacked">\r\n                <li><a href="/homepage/Users/">View All Users</a></li>\r\n\r\n\r\n            </ul>\r\n        </nav>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<br>\r\n<br>\r\n<a href="/homepage/Users.Create" class="btn btn-warning">Create new user</a>\r\n<br>\r\n<br>\r\n<table class="table table-striped">\r\n<tr>\r\n    <th>ID</th>\r\n    <th>First Name</th>\r\n    <th>Last Name</th>\r\n    <th>Email</th>\r\n    <th>Action</th>\r\n</tr>\r\n\r\n')
        for User in users:
            __M_writer('    <tr>\r\n        <td>')
            __M_writer(str( User.id ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( User.first_name ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( User.last_name ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( User.email ))
            __M_writer('</td>\r\n        <td><a href ="/homepage/Users.edit/')
            __M_writer(str( User.id ))
            __M_writer('">Edit</a> | <a href="/homepage/Users.Delete/')
            __M_writer(str( User.id ))
            __M_writer('">Delete</a> | <a href="/homepage/Users.ChangePermissions/')
            __M_writer(str( User.id ))
            __M_writer('">Permissions</a></td>\r\n    </tr>\r\n')
        __M_writer('</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 9, "72": 9, "73": 24, "74": 25, "75": 26, "76": 26, "77": 27, "78": 27, "79": 28, "80": 28, "81": 29, "82": 29, "83": 30, "84": 30, "85": 30, "86": 30, "87": 30, "88": 30, "89": 33, "27": 0, "95": 89, "37": 1, "42": 34, "47": 46, "53": 35, "59": 35}, "uri": "Users.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\homepage\\templates/Users.html"}
__M_END_METADATA
"""
