from odoo import models,fields
class calories_model(models.Model):
    _name = 'calories_model.calories_model'
    _inherit = 'calories_model.calories_model'

    pro_calories = fields.Integer('product calories')

