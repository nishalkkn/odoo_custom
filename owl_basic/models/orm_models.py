from odoo import fields,models,api

class OrmModel(models.Model):
    _name = "orm.model"

    @api.model
    def search_sale_order(self):
         demo = self.env['sale.order'].search([],limit=10)
         return demo