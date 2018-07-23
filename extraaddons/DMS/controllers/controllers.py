# -*- coding: utf-8 -*-
from odoo import http

# class Mymodule(http.Controller):
#     @http.route('/DMS/DMS/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/DMS/DMS/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('DMS.listing', {
#             'root': '/DMS/DMS',
#             'objects': http.request.env['DMS.DMS'].search([]),
#         })

#     @http.route('/DMS/DMS/objects/<model("DMS.DMS"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('DMS.object', {
#             'object': obj
#         })