from odoo import models,fields

class consignee_info(models.Model):
    _name = 'consignee_info.consignee_info'
    _description = 'contains Consignee Information'

    consignee_name = fields.Char('Consignee Name')
    consignee_address = fields.Char(string='Address')

    consignee_tel = fields.Char('Tel')
    consignee_fax = fields.Char('Fax')
    consignee_email = fields.Char('Email')
    consignee_salesperson = fields.Char('Salesperson')

