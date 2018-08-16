from odoo import models,fields,api

class charges_model(models.Model):
    _name = 'charges_model.charges_model'

    charge = fields.Char('Charges')
    charge_value = fields.Float('Value')
    #charge_connect = fields.One2many('illing_master_info.filling_master_info', 'charge item')