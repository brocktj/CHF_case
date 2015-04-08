# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428464086.64478
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Account\\templates/Account.Admin.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h1>Admin Page</h1>\r\n<p>Welcome ')
        __M_writer(str( user.first_name ))
        __M_writer(' ')
        __M_writer(str( user.last_name))
        __M_writer(' </p>\r\n\r\n<table class="table table-striped">\r\n    <tr>\r\n        <td>\r\n            Username\r\n        </td>\r\n        <td>\r\n            ')
        __M_writer(str( user.username ))
        __M_writer('\r\n        </td>\r\n    </tr>\r\n    <tr>\r\n        <td>\r\n            Name\r\n        </td>\r\n        <td>\r\n            ')
        __M_writer(str( user.first_name ))
        __M_writer(' ')
        __M_writer(str( user.last_name ))
        __M_writer('\r\n        </td>\r\n    </tr>\r\n    <tr>\r\n        <td>\r\n            Address\r\n        </td>\r\n        <td>\r\n            <p>')
        __M_writer(str( user.address ))
        __M_writer('</p>\r\n            <p>')
        __M_writer(str( user.city ))
        __M_writer('</p>\r\n            <p>')
        __M_writer(str( user.state ))
        __M_writer('</p>\r\n            <p>')
        __M_writer(str( user.zip ))
        __M_writer('</p>\r\n        </td>\r\n    </tr>\r\n\r\n\r\n</table>\r\n<div><a href="/Account/Account.update_password">Change Password</a></div>\r\n<div><a href="/Account/Account.edit_user_info" class="btn btn-success">Update your information</a></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 29, "65": 29, "66": 30, "67": 30, "68": 31, "69": 31, "70": 32, "71": 32, "77": 71, "27": 0, "35": 1, "40": 40, "46": 3, "53": 3, "54": 5, "55": 5, "56": 5, "57": 5, "58": 13, "59": 13, "60": 21, "61": 21, "62": 21, "63": 21}, "uri": "Account.Admin.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Account\\templates/Account.Admin.html"}
__M_END_METADATA
"""
