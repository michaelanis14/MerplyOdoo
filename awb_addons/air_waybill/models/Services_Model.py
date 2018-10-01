# -*- coding: utf-8 -*-
import dp as dp

from odoo import models,fields,api
class Services_Model(models.Model):
    _inherit = "product.template"
    _rec_name = 'service_name'
    _description = 'Services Information'



    #afb_sevices_IDs = fields.Many2one('account.invoice')


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
                                     ],default='f_ch', index=True, required=True, translate=True)

    type = fields.Selection([
        ('consu','Consumable'),
        ('service','Service')], string='Product Type', default='service', required=True,
        help='A stockable product is a product for which you manage stock. The "Inventory" app has to be installed.\n'
             'A consumable product, on the other hand, is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.\n'
             'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
             'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')

    main = fields.Boolean('Main')

    lump_sum = fields.Boolean('Lumb Sum')




