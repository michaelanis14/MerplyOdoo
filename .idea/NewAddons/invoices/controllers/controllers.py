# -*- coding: utf-8 -*-
from odoo import http

# class Invoices(http.Controller):
#     @http.route('/invoices/invoices/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoices/invoices/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoices.listing', {
#             'root': '/invoices/invoices',
#             'objects': http.request.env['invoices.invoices'].search([]),
#         })

#     @http.route('/invoices/invoices/objects/<model("invoices.invoices"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoices.object', {
#             'object': obj
#         })