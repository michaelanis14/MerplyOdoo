from odoo import models, fields


class Invoice_info(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    mawb = fields.Char('MAWB')
    hawb = fields.Char('HAWB')

