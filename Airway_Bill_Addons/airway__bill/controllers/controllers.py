# -*- coding: utf-8 -*-
from odoo import http

# class AirwayBill(http.Controller):
#     @http.route('/AWBmodel/AWBmodel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/AWBmodel/AWBmodel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('AWBmodel.listing', {
#             'root': '/AWBmodel/AWBmodel',
#             'objects': http.request.env['AWBmodel.AWBmodel'].search([]),
#         })

#     @http.route('/AWBmodel/AWBmodel/objects/<model("AWBmodel.AWBmodel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('AWBmodel.object', {
#             'object': obj
#         })