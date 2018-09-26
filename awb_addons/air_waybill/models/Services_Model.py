# -*- coding: utf-8 -*-
import dp as dp

from odoo import models,fields,api
class Services_Model(models.Model):
    _inherit = "product.template"
    _rec_name = 'service_name'
    _description = 'Services Information'



    #afb_sevices_IDs = fields.Many2one('account.invoice')

    service_name = fields.Selection([('f_ch', 'FOB Charges (EX-Works)'),
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
                                     ],default='f_ch')
    main = fields.Boolean('Main')

    lump_sum = fields.Boolean('Lumb Sum')


