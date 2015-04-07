# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428447749.950356
_enable_loop = True
_template_filename = '/Users/brock/Documents/CHF_case/sprint0/Store/templates/WardrobeItem.get_late_items.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        late_items_30 = context.get('late_items_30', UNDEFINED)
        late_items_90 = context.get('late_items_90', UNDEFINED)
        late_items_60 = context.get('late_items_60', UNDEFINED)
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
        def content():
            return render_content(context)
        late_items_30 = context.get('late_items_30', UNDEFINED)
        late_items_90 = context.get('late_items_90', UNDEFINED)
        late_items_60 = context.get('late_items_60', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="/Store/WardrobeItem.send_late_emails" class="btn btn-success">Send Email Notices</a>\n<a href="/Store/WardrobeItem.send_late_texts" class="btn btn-success">Send SMS Notices</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Size</th>\n        <th>Date out</th>\n        <th>Date Due</th>\n        <th></th>\n    </tr>\n    <tr>\n        <td>Over 30 days late</td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n    </tr>\n\n')
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
            __M_writer('</td>\n')
            if RentedLineItem.transaction_ID is not None:
                __M_writer('        <td>')
                __M_writer(str( RentedLineItem.transaction_ID.customer.first_name ))
                __M_writer(' ')
                __M_writer(str( RentedLineItem.transaction_ID.customer.last_name ))
                __M_writer('</td>\n')
            __M_writer('\n\n    </tr>\n')
        __M_writer('\n    <tr>\n        <td>Over 60 days late</td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n    </tr>\n')
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
            __M_writer('</td>\n')
            if RentedLineItem.transaction_ID is not None:
                __M_writer('        <td>')
                __M_writer(str( RentedLineItem.transaction_ID.customer.first_name ))
                __M_writer(' ')
                __M_writer(str( RentedLineItem.transaction_ID.customer.last_name ))
                __M_writer('</td>\n')
            __M_writer('\n\n    </tr>\n')
        __M_writer('    <tr>\n        <td>Over 90 days late</td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n        <td></td>\n    </tr>\n')
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
            __M_writer('</td>\n')
            if RentedLineItem.transaction_ID is not None:
                __M_writer('        <td>')
                __M_writer(str( RentedLineItem.transaction_ID.customer.first_name ))
                __M_writer(' ')
                __M_writer(str( RentedLineItem.transaction_ID.customer.last_name ))
                __M_writer('</td>\n')
            __M_writer('\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 92, "129": 96, "135": 129, "16": 2, "29": 0, "39": 1, "40": 2, "45": 97, "51": 10, "60": 10, "61": 31, "62": 32, "63": 33, "65": 33, "66": 35, "67": 35, "68": 36, "69": 36, "70": 37, "71": 37, "72": 38, "73": 38, "74": 39, "75": 39, "76": 40, "77": 41, "78": 41, "79": 41, "80": 41, "81": 41, "82": 43, "83": 47, "84": 56, "85": 57, "86": 58, "88": 58, "89": 60, "90": 60, "91": 61, "92": 61, "93": 62, "94": 62, "95": 63, "96": 63, "97": 64, "98": 64, "99": 65, "100": 66, "101": 66, "102": 66, "103": 66, "104": 66, "105": 68, "106": 72, "107": 80, "108": 81, "109": 82, "111": 82, "112": 84, "113": 84, "114": 85, "115": 85, "116": 86, "117": 86, "118": 87, "119": 87, "120": 88, "121": 88, "122": 89, "123": 90, "124": 90, "125": 90, "126": 90, "127": 90}, "filename": "/Users/brock/Documents/CHF_case/sprint0/Store/templates/WardrobeItem.get_late_items.html", "source_encoding": "ascii", "uri": "WardrobeItem.get_late_items.html"}
__M_END_METADATA
"""
