from odoo import models, fields


class Doctor(models.Model):
    _inherit = 'hr.employee'

    room_no = fields.Char(string="Room no")
    fee = fields.Integer(string="Fee")
    age= fields.Integer(string="Age")



