from odoo import models,fields,api
class Edit_product_Template(models.Model):
    _inherit = 'product.product'
    _description = 'Editting Product template'

    sale_ok = fields.Boolean(
        'Can be Sold', default=False,
        help="Specify if the product can be selected in a sales order line.")

    purchase_ok = fields.Boolean('Can be Purchased', default=False)

    type = fields.Selection([
        ('consu', ('Consumable')),
        ('service', ('Service'))], string='Product Type', default='service', required=True,
        help='A stockable product is a product for which you manage stock. The "Inventory" app has to be installed.\n'
             'A consumable product, on the other hand, is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.\n'
             'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
             'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')