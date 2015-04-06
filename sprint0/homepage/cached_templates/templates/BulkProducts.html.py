# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422995036.211293
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/BulkProducts.html'
_template_uri = 'BulkProducts.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        blkProducts = context.get('blkProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n<a href="/homepage/WardrobeItem.Create">Create new user</a>\n<table>\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Start Date</th>\n        <th>End Date</th>\n    </tr>\n')
        for BulkProduct in blkProducts:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( BulkProduct.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.quantity_on_hand ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( BulkProduct.current_price ))
            __M_writer('</td>\n        <td> <a href="/homepage/BulkProducts.edit/')
            __M_writer(str( BulkProduct.id ))
            __M_writer('">Edit</a> | Delete </td>\n\n    </tr>\n')
        __M_writer('</table>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "BulkProducts.html", "filename": "/Users/brock/sprint0/homepage/templates/BulkProducts.html", "source_encoding": "ascii", "line_map": {"32": 22, "33": 23, "34": 23, "35": 24, "36": 24, "37": 28, "43": 37, "16": 0, "22": 1, "23": 17, "24": 18, "25": 19, "26": 19, "27": 20, "28": 20, "29": 21, "30": 21, "31": 22}}
__M_END_METADATA
"""
