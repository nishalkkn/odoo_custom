from odoo import models, fields


class ProductRatingField(models.Model):
    _inherit = "product.template"

    product_rating = fields.Selection([('poor','Poor'),('fair','Fair'),('good','Good'),('very_good','Very Good'),('excellent','Excellent')],help="Rating of the product")
