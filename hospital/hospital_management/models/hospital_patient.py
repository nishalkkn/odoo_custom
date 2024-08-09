from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    department_name = fields.Char(string="Department")
    blood_group = fields.Selection([('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('Ab+','Ab+'),('AB-','AB-')])
    date_of_birth = fields.Date(string="Date of birth")
    age = fields.Integer(string="Age")
