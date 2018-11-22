# -*- coding: utf-8 -*-
from odoo import http

# class FreightModule(http.Controller):
#     @http.route('/freight_module/freight_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/freight_module/freight_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('freight_module.listing', {
#             'root': '/freight_module/freight_module',
#             'objects': http.request.env['freight_module.freight_module'].search([]),
#         })

#     @http.route('/freight_module/freight_module/objects/<model("freight_module.freight_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('freight_module.object', {
#             'object': obj
#         })