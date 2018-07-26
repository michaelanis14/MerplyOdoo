# -*- coding: utf-8 -*-

from odoo import models, fields, api

class diet_meal(models.Model):
     _name = 'diet_meal.diet_meal'

     name = fields.Char('Meal Name')
     meal_date = fields.Datetime('Meal Date')
     user_id = fields.Many2one('res.users', 'User Meal ID')
     description = fields.Text('Meal Note')
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100