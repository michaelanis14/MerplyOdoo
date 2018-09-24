# -*- coding: utf-8 -*-
import dp as dp

from odoo import models,fields,api
class Cargo_Model(models.Model):
    _name = 'services.model'
    _inherit = "account.invoice.line"
    _rec_name = 'service_name'
    _description = 'Services Information'



    #afb_sevices_IDs = fields.Many2one('account.invoice')
    sevice_ID = fields.Many2one('services.model')

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
    sale = fields.Float('Sale')
    main = fields.Boolean('Main')

    description = fields.Text('Description')
    vendor =fields.Char('Vendor')
    lump_sum = fields.Boolean('Lumb Sum')

    tax_id = fields.Many2one('account.tax', string='Tax', ondelete='restrict')

    supplier_taxes_id = fields.Many2one('account.tax', string='Vendor Taxes', ondelete='restrict')


# overriding compute_price
    @api.one
    @api.depends('cost', 'discount', 'invoice_line_tax_ids',
#ana 7azaft el quantity w elproduct id 34an kida kida hoa 7atethom b none lo mada5alo4
        'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
        'invoice_id.date_invoice', 'invoice_id.date')
    def _compute_price(self):
        currency = self.invoice_id and self.invoice_id.currency_id or None
        price = self.cost * (1 - (self.discount or 0.0) / 100.0)
        taxes = False
        if self.invoice_line_tax_ids:
            taxes = self.invoice_line_tax_ids.compute_all(price, currency, partner=self.invoice_id.partner_id)  #----> d fun bt7sb eltaxes lkol elproducts elly da5lt (4elt bardo el product id w elquantity)
        self.price_subtotal = price_subtotal_signed = taxes['total_excluded'] if taxes else self.price
        self.price_total = taxes['total_included'] if taxes else self.price_subtotal
        if self.invoice_id.currency_id and self.invoice_id.currency_id != self.invoice_id.company_id.currency_id:
            price_subtotal_signed = self.invoice_id.currency_id.with_context(date=self.invoice_id._get_currency_rate_date()).compute(price_subtotal_signed, self.invoice_id.company_id.currency_id)
        sign = self.invoice_id.type in ['in_refund', 'out_refund'] and -1 or 1
        self.price_subtotal_signed = price_subtotal_signed * sign
