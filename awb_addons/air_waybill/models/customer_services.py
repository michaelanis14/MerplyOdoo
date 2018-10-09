import dp

from odoo import models,fields,api

class customer_services(models.Model):
    _name = 'services.info'
    _description = 'Services names and costs'

    afb_id = fields.Many2one('account.invoice')
    custom_service_name = fields.Selection([('f_ch', 'FOB Charges (EX-Works)'),
                             ('fuel', 'FUEL'),
                             ('sec', 'SEC'),
                             ('fuel_sec', 'FUEL & SEC'),
                             ('courier', 'COURIR'),
                             ('eur', 'EUR 1'),
                             ('eur', 'EUR 1'),
                             ('x_ray', 'X-RAY'),
                             ('dgr', 'DGR'),
                             ('awb', 'AWB'),
                             ('customs', 'CUSTOMS'),
                             ('goods_cost', 'COST OF GOODS'),
                             ('pick', 'PICK UP'),
                             ('packing', 'PACKING'),
                             ('packaging', 'PACKAGING'),
                             ('sv_charges', 'S.V CHARGES'),
                             ('handling', 'HANDLING'),
                             ('special', 'SPECIAL TRUCK'),
                             ('inspection', 'INSPECTION'),
                             ('fumigation', 'FUMIGATION'),
                             ('leg_cost', 'COST OF LEGALIZATION'),
                             ('clearance', 'CLEARANCE'),
                             ('origin', 'CERTIFICATE OF ORIGIN'),
                             ('collection', 'COLLECTION'),
                             ], default='f_ch', index=True, required=True, translate=True)

    hawb_cs_ID = fields.Many2one("hawb.model",string='HAWB NO')
    #customer_currency = fields.Many2one(related='afb_id.foreign_cur', store=True, readonly=True)

    custom_service_cost = fields.Float(string='Customer Service Cost', required=True)
    #total_cost = fields.Monetary(string='Total cost', store=True, readonly=True, currency_field='customer_currency',compute='_compute_total_cost')




