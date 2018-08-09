from odoo import models, fields


class Invoice_info(models.Model):
    _name = 'account.invoice.line'
    _inherit = 'account.invoice.line'

    package_no = fields.Integer('Package')
    net_weight = fields.Float('Net Weight')
    gross_weight = fields.Float('Gross Weight')

