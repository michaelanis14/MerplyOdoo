# -*- coding: utf-8 -*-
from odoo import http

# class ProductCalorieModule(http.Controller):
#     @http.route('/caloriesmodule/caloriesmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caloriesmodule/caloriesmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caloriesmodule.listing', {
#             'root': '/caloriesmodule/caloriesmodule',
#             'objects': http.request.env['caloriesmodule.caloriesmodule'].search([]),
#         })

#     @http.route('/caloriesmodule/caloriesmodule/objects/<model("caloriesmodule.caloriesmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caloriesmodule.object', {
#             'object': obj
#         })