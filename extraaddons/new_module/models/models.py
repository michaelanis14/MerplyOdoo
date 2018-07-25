# -*- coding: utf-8 -*-

from odoo import models, fields, api

class new_module(models.Model):
     _name = 'product.template'
     _inherit = 'product.template'

     calories = fields.Integer('product calories')
     fat = fields.Float('product fat')
     servingSize= fields.Float('Serving Size')
     lastUpdate = fields.Date('Last Update')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100