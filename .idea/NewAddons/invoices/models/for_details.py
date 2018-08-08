from odoo import models, fields

class for_details(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    chipper = fields.Text()
    Consignee = fields.Selection(selection=[

        ('agent1', 'Agent 1'),

        ('agent2', 'Agent 2'), ],
        string='Consignee')

    Exporting_carrier = fields.Char("Exporting Carrier")
    Exporting_date = fields.Date("Exporting Date")

    Intermediate_consignee = fields.Selection(selection=[

        ('agent1', 'Agent 1'),

        ('agent2', 'Agent 2'), ],
        string='Intermediate Consignee')

