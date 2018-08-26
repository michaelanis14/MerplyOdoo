# -*- coding: utf-8 -*-

from odoo import models, fields, api

class filling_master_info(models.Model):
    _name = 'filling_master_info.filling_master_info'

    consignee = fields.Many2one('consignee_info.consignee_info','Consignee')

    mawb = fields.Char('MAWB NO')
    hawb = fields.Char('HAWB NO')

    no_of_packages = fields.Integer('No Of Packages')
    gross_weight = fields.Float('Gross Weight')
    net_weight = fields.Float('Net Weight')

    date = fields.Date('Invoice Date')
    delivery_order = fields.Char('Delivery Order')

    destination_airport = fields.Char('Airport of Destination')
    departure_airport = fields.Char('Airport of Departure')
    charge_id = fields.Many2one('charges_model.charges_model', 'Charges')
    amount = fields.Float(string='Amount', store='true', compute='_compute_Amount')

    @api.one
    @api.depends('charge_id')
    def _compute_Amount(self):
        for  sinle_charge in self.charge_id:
            current_charge=0
            current_charge = current_charge + self.charge_id.charge_value
            self.amount = current_charge













