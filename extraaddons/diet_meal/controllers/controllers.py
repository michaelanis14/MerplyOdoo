# -*- coding: utf-8 -*-
from odoo import http

# class DietMeal(http.Controller):
#     @http.route('/diet_meal/diet_meal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diet_meal/diet_meal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('diet_meal.listing', {
#             'root': '/diet_meal/diet_meal',
#             'objects': http.request.env['diet_meal.diet_meal'].search([]),
#         })

#     @http.route('/diet_meal/diet_meal/objects/<model("diet_meal.diet_meal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diet_meal.object', {
#             'object': obj
#         })