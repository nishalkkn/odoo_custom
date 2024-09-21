from odoo import models, fields


class ProductRatingField(models.Model):
    _inherit = "product.product"

    product_rating = fields.Selection([('poor','Poor'),('fair','Fair'),('good','Good'),('very_good','Very Good'),('excellent','Excellent')],help="Rating of the product")
    demo = fields.Char()


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('product_rating')
        return result
