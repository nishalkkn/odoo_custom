from odoo import models, fields


class Department(models.Model):
    _inherit = 'hr.department'

    block = fields.Char(string="Block")
    doctor = fields.Many2many('hr.employee', string="Doctor")
