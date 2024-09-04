from odoo import models, fields, api


class Tolerance(models.Model):
    _inherit = 'res.partner'

    tolerance = fields.Float('Tolerance', help="Tolerance for customer")
    max_tolerance = fields.Float('Maximum Tolerance')
    tolerance_percentage = fields.Float('Tolerance percentage', compute='_compute_tolerance_percentage',
                                        inverse='_inverse_tolerance_percentage')

    @api.depends('tolerance', 'max_tolerance')
    def _compute_tolerance_percentage(self):
        """compute function for finding tolerance percentage"""
        for rec in self:
            if rec.max_tolerance > 0:
                rec.tolerance_percentage = rec.tolerance / rec.max_tolerance

    def _inverse_tolerance_percentage(self):
        """inverse function for tolerance percentage"""
        if self.tolerance_percentage:
            self.tolerance = self.max_tolerance * self.tolerance_percentage
