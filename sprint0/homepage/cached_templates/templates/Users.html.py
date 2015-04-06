# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425715546.975716
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/Users.html'
_template_uri = 'Users.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="/homepage/Users.Create">Create new user</a>\n<table class="table table-striped">\n<tr>\n    <th>ID</th>\n    <th>First Name</th>\n    <th>Last Name</th>\n    <th>Email</th>\n    <th>Action</th>\n</tr>\n\n')
        for User in users:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( User.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( User.first_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( User.last_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( User.email ))
            __M_writer('</td>\n        <td><a href ="/homepage/Users.edit/')
            __M_writer(str( User.id ))
            __M_writer('">Edit</a> | <a href="/homepage/Users.Delete/')
            __M_writer(str( User.id ))
            __M_writer('">Delete</a> | <a href="/homepage/Users.ChangePermissions/')
            __M_writer(str( User.id ))
            __M_writer('">Permissions</a></td>\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/homepage/Users/">View All Users</a></li>\n                <li><a href="">View Administrators</a></li>\n                <li><a href="">View Managers</a></li>\n\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/homepage/templates/Users.html", "line_map": {"64": 22, "65": 23, "66": 23, "67": 24, "68": 24, "69": 25, "70": 25, "71": 26, "72": 26, "73": 26, "74": 26, "75": 26, "76": 26, "77": 29, "83": 31, "89": 31, "27": 0, "95": 89, "37": 1, "42": 30, "47": 43, "53": 9, "60": 9, "61": 20, "62": 21, "63": 22}, "source_encoding": "ascii", "uri": "Users.html"}
__M_END_METADATA
"""
