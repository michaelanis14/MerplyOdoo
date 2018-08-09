from odoo import models, fields

class Consignee_info(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    consignee_name = fields.Selection(selection=[

        ('agent1', 'Agent 1'),

        ('agent2', 'Agent 2'), ],
        string='Consignee')

    freight_charges = fields.Float('Freight Charges')
    discharge_expenses = fields.Float('Discharge Expenses')
    exw = fields.Float('ExWorks Charges')
    fob = fields.Float('FOB Charges')


