# -*- coding: utf-8 -*-
from odoo import http

# class Awbinvoices(http.Controller):
#     @http.route('/awbinvoices/awbinvoices/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/awbinvoices/awbinvoices/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('awbinvoices.listing', {
#             'root': '/awbinvoices/awbinvoices',
#             'objects': http.request.env['awbinvoices.awbinvoices'].search([]),
#         })

#     @http.route('/awbinvoices/awbinvoices/objects/<model("awbinvoices.awbinvoices"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('awbinvoices.object', {
#             'object': obj
#         })