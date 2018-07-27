# -*- coding: utf-8 -*-

from odoo import models, fields, api

class diet_meal(models.Model):
     _name = 'diet_meal.diet_meal'

     name = fields.Char('Meal Name')
     meal_date = fields.Datetime('Meal Date')
     user_id = fields.Many2one('res.users', 'User Meal ID')
     description = fields.Text('Meal Note')


class meal_items(models.Model):
     _name = 'meal_items.meal_items'

     name = fields.Char('Meal Name')
     meal_date = fields.Datetime('Meal Date')
     item_id = fields.Many2one('product.template')
     servings = fields.Float('Item Servings')
     description = fields.Text('Item Note')