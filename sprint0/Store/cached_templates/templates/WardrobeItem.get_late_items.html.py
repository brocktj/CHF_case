# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428365906.044452
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/WardrobeItem.get_late_items.html'
_template_uri = 'WardrobeItem.get_late_items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import homepage.models as hmod 

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
        late_items_60 = context.get('late_items_60', UNDEFINED)
        late_items_30 = context.get('late_items_30', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        late_items_90 = context.get('late_items_90', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        late_items_60 = context.get('late_items_60', UNDEFINED)
        late_items_30 = context.get('late_items_30', UNDEFINED)
        def content():
            return render_content(context)
        late_items_90 = context.get('late_items_90', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="/Store/WardrobeItem.send_late_emails" class="btn btn-success">Send Email Notices</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Size</th>\n        <th>Date out</th>\n        <th>Date Due</th>\n    </tr>\n    <tr>\n        <td>Over 30 days late</td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n    </tr>\n\n')
        for RentedLineItem in late_items_30:
            __M_writer('\n        ')
            rentedItem = hmod.WardrobeItem.objects.get(id=RentedLineItem.wardrobe_item_ID.id) 
            
            __M_writer('\n    <tr>\n        <td>')
            __M_writer(str( rentedItem.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( rentedItem.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( rentedItem.size ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_out ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_due ))
            __M_writer('</td>\n\n\n    </tr>\n')
        __M_writer('\n    <tr>\n        <td>Over 60 days late</td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n    </tr>\n')
        for RentedLineItem in late_items_60:
            __M_writer('\n        ')
            rentedItem = hmod.WardrobeItem.objects.get(id=RentedLineItem.wardrobe_item_ID.id) 
            
            __M_writer('\n    <tr>\n        <td>')
            __M_writer(str( rentedItem.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( rentedItem.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( rentedItem.size ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_out ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_due ))
            __M_writer('</td>\n\n\n    </tr>\n')
        __M_writer('    <tr>\n        <td>Over 90 days late</td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n\n    </tr>\n')
        for RentedLineItem in late_items_90:
            __M_writer('\n        ')
            rentedItem = hmod.WardrobeItem.objects.get(id=RentedLineItem.wardrobe_item_ID.id) 
            
            __M_writer('\n    <tr>\n        <td>')
            __M_writer(str( rentedItem.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( rentedItem.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( rentedItem.size ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_out ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_due ))
            __M_writer('</td>\n\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "WardrobeItem.get_late_items.html", "line_map": {"16": 2, "29": 0, "39": 1, "40": 2, "45": 84, "51": 10, "60": 10, "61": 28, "62": 29, "63": 30, "65": 30, "66": 32, "67": 32, "68": 33, "69": 33, "70": 34, "71": 34, "72": 35, "73": 35, "74": 36, "75": 36, "76": 41, "77": 49, "78": 50, "79": 51, "81": 51, "82": 53, "83": 53, "84": 54, "85": 54, "86": 55, "87": 55, "88": 56, "89": 56, "90": 57, "91": 57, "92": 62, "93": 70, "94": 71, "95": 72, "97": 72, "98": 74, "99": 74, "100": 75, "101": 75, "102": 76, "103": 76, "104": 77, "105": 77, "106": 78, "107": 78, "108": 83, "114": 108}, "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/WardrobeItem.get_late_items.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
