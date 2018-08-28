# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dietfacts(models.Model):
     _name = 'product.template'
     _inherit = 'product.template'


     calories = fields.Integer()
     serving_size = fields.Float("Serving Size")
     last_update = fields.Date('Last Update')
     dietitem = fields.Boolean('Diet Item')


class users_meals(models.Model):
     _name = "users.meals"

     mealName = fields.Char("Meal Name")
     mealDate = fields.Datetime("Meal Time")
     mealUser = fields.Many2one('res.users', 'Meal User')
     mealItems = fields.One2many("meals.items", 'mealItemsName', 'Meal Items')
     totalMealCalories = fields.Integer(string='Calories per Meal', store= True, compute = '_calCalories')

     @api.one
     @api.depends('mealItems', 'mealItems.servings')
     def _calCalories(self):
         currentcalories = 0
         for item in self.mealItems:

            currentcalories= currentcalories + (item.selecteMealIteams.calories * item.servings)

            self.totalMealCalories= currentcalories


class meal_items(models.Model):
     _name = "meals.items"

     mealItemsName = fields.Many2one('users.meals', 'Meal Name')
     selecteMealIteams = fields.Many2one('product.template', 'Add your Meal Items')
     servings = fields.Float('Servings')
     itemCalories = fields.Integer(related = 'selecteMealIteams.calories', string='Item Calories', store=True, readonly=True)

