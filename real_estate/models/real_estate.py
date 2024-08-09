from odoo import models, fields


class RealEstate(models.Model):
    _name = "real.estate"
    _description = "Real Estate"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    expected_price = fields.Float()
    bedrooms = fields.Integer(default="2")
    facades = fields.Integer()
    garden = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('option1', 'New'), ('option2', 'Offer Received'), ('option3', 'Offer Accepted'), ('option4', 'Sold'),
         ('option5', 'Canceled')])
    available_from = fields.Date(copy=False, default=fields.Date.today())
    selling_price = fields.Integer(readonly=True, default="50", copy=False)
    living_area = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
