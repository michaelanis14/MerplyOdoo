import uuid

import dp

from odoo import models,fields,api

class Air_freight_bill(models.Model):
    _inherit = 'account.invoice'
    _description = 'Air Freight Bill in foreign currency'


class Air_invoice_line(models.Model):
    _inherit =  "account.invoice.line"

    name = fields.Selection([('f_ch', 'FOB Charges (EX-Works)'),
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
                             ], default='f_ch', index=True, required=True, translate=True,string=' Service ')
