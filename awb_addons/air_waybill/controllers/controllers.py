# -*- coding: utf-8 -*-
from odoo import http

# class AirWaybill(http.Controller):
#     @http.route('/air_waybill/air_waybill/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/air_waybill/air_waybill/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('air_waybill.listing', {
#             'root': '/air_waybill/air_waybill',
#             'objects': http.request.env['air_waybill.air_waybill'].search([]),
#         })

#     @http.route('/air_waybill/air_waybill/objects/<model("air_waybill.air_waybill"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('air_waybill.object', {
#             'object': obj
#         })