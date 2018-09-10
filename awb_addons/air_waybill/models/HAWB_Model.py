from odoo import models,fields,api

class HAWB_Model(models.Model):
    _name = 'hawb.model'
    _description = 'HAWB Model'

    mawb_IDs = fields.Many2one("mawb.model")
    hawb_no = fields.Char(string='HAWB Number')
    airD = fields.Char(related='mawb_IDs.airport_of_departure',
                       string='Airport of Departure',
                       store = True, readonly = True)