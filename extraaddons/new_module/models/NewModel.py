# -*- coding: utf-8 -*-

from odoo import models, fields, api

class new_module(models.Model):
     _name = 'new_module.new_module'

     calories = fields.Integer('product calories')
     fat = fields.Float('product fat')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100