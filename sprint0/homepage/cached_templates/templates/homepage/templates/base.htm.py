# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428448430.998784
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footer', 'left', 'header']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n<meta name="description" content="Colonial heritage page website, store and information pages">\r\n<meta name="keywords" content="Colonial,Heritage,Foundation,Utah,Historical,Reenactment,History,enrichment,generations">\r\n<head>\r\n\r\n\r\n\r\n')
        __M_writer('\r\n\r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\r\n    <link rel="icon" type="image/x-icon"\r\n          href="http://fc07.deviantart.net/fs70/f/2012/185/5/f/triforce_icon_free_to_use_by_kittyzelda64-d560tnh.png"/>\r\n\r\n    <title>Colonial Heritage Foundation; Preserving History</title>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context) ))
        __M_writer('\r\n\r\n</head>\r\n\r\n\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\r\n<br>\r\n<br>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n<div class="container-fluid">\r\n    <div id="center" class="col-md-8">\r\n\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n<div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n  <div class="modal-dialog">\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        ...\r\n      </div>\r\n      <div class="modal-footer">\r\n\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n</div>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str( static_renderer.get_template_js(request, context) ))
        __M_writer('\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<nav class="navbar navbar-inverse navbar-fixed-top">\r\n    <div class="container">\r\n        <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"\r\n                    aria-expanded="false" aria-controls="navbar">\r\n                <span class="sr-only">Toggle navigation</span>\r\n                <span class="icon-bar"></span>\r\n                <span class="icon-bar"></span>\r\n                <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand" href="/homepage">Colonial Heritage Foundation <small>preserving history</small></a>\r\n        </div>\r\n        <div id="navbar" class="collapse navbar-collapse">\r\n            <ul class="nav navbar-nav">\r\n\r\n\r\n')
        if request.user.username != '':
            __M_writer('                <li><a href="/homepage/Users/">Account</a></li>\r\n                <li><a href="/Store/StoreView/">Store</a></li>\r\n                <li><a href="/homepage/Events/">Events</a></li>\r\n\r\n')
            if request.user.groups.filter(name='AdminGroup').exists():
                __M_writer('                <li><a href="/Store/WardrobeItem.get_late_items/" id="generate_report">Late Items</a></li>\r\n')
            else:
                __M_writer('\r\n')
            __M_writer('\r\n                <li><a href ="/Account/logout">Logout</a></li>\r\n                <li><a>Welcome: ')
            __M_writer(str( request.user.username ))
            __M_writer('</a></li>\r\n\r\n')
        else:
            __M_writer('                <li><a id="show_modal" href="#" class="text-right">Login</a></li>\r\n\r\n')
        __M_writer('\r\n            </ul>\r\n        </div>\r\n    </div>\r\n</nav>\r\n\r\n<div class="btn-group">\r\n    <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">\r\n        Action <span class="caret"></span>\r\n    </button>\r\n    <ul class="dropdown-menu" role="menu">\r\n        <li><a href="#">Action</a></li>\r\n        <li><a href="#">Another action</a></li>\r\n        <li><a href="#">Something else here</a></li>\r\n        <li class="divider"></li>\r\n        <li><a href="#">Separated link</a></li>\r\n    </ul>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0/homepage/templates/base.htm", "source_encoding": "ascii", "line_map": {"128": 66, "129": 68, "130": 69, "131": 72, "68": 124, "69": 126, "70": 126, "137": 131, "82": 101, "76": 101, "16": 4, "18": 0, "127": 66, "88": 122, "100": 95, "125": 62, "122": 59, "94": 122, "112": 36, "34": 2, "35": 4, "36": 5, "40": 5, "41": 17, "42": 21, "43": 21, "44": 23, "45": 23, "46": 30, "47": 30, "48": 30, "53": 90, "119": 36, "120": 54, "121": 55, "58": 97, "123": 60, "124": 61, "106": 95, "126": 64, "63": 103}, "uri": "/homepage/templates/base.htm"}
__M_END_METADATA
"""
