from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    machine_id = fields.One2many('machine.management','customer_id', string="Machine")
    alternative_cust = fields.Many2many('machine.management',compute="employee_count")

    # domain setting for machine_id
    @api.depends('name')
    def employee_count(self):
        self.alternative_cust = self.env['machine.management'].search([('customer_id', '=', self.name)])


