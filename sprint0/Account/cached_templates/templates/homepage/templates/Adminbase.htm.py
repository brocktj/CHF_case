# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428178631.343226
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/Adminbase.htm'
_template_uri = '/homepage/templates/Adminbase.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content', 'footer', 'header']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n\n<!DOCTYPE html>\n<html>\n<meta charset="UTF-8">\n<meta name="description" content="Colonial heritage page website, store and information pages">\n<meta name="keywords" content="Colonial,Heritage,Foundation,Utah,Historical,Reenactment,History,enrichment,generations">\n<head>\n\n    <title>homepage</title>\n\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context) ))
        __M_writer('\n\n</head>\n\n\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n</div>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n<div class = "container-fluid">\n<div id="center" class="col-md-8">\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</div>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n\n<div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n      </div>\n      <div class="modal-body">\n      </div>\n      <div class="modal-footer">\n\n      </div>\n    </div>\n  </div>\n</div>\n')
        __M_writer(str( static_renderer.get_template_js(request, context) ))
        __M_writer('\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/homepage/Events/">Events</a></li>\n                <li><a href="/homepage/Users//">Users</a></li>\n                <li><a href="/Store/Store/">Store Items</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n<div class ="jimbob">\n<p><a href="http://localhost:8000/homepage/terms/">terms and conditions</a> </p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="page-header">\n    <h1>The Colonial Heritage Foundation <small>preserving history</small></h1>\n    <p><a href="/Account/logout/">Logout</a></p>\n    <button id="show_modal">Log in</button>\n    <button id="generate_report">Late Items</button>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/homepage/templates/Adminbase.htm", "line_map": {"67": 65, "68": 83, "69": 83, "75": 41, "16": 3, "81": 41, "18": 0, "99": 61, "87": 56, "111": 30, "93": 56, "34": 3, "35": 4, "39": 4, "40": 17, "41": 19, "42": 19, "43": 21, "44": 21, "45": 24, "46": 24, "47": 24, "52": 37, "117": 30, "105": 61, "57": 52, "123": 117, "62": 59}, "uri": "/homepage/templates/Adminbase.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
