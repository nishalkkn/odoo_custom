from odoo import models, fields, api


class Consult(models.Model):
    _name = "hospital.consultation"
    _description = " Hospital consultation"

    date = fields.Date(default=fields.Date.today())
    token_no = fields.Many2one('hospital.op.ticket', string="Op no")
    patient = fields.Many2one('res.partner', required=True, string="Patient")
    doctor = fields.Many2one('hr.employee', required=True, string="Doctor")
    age = fields.Integer(string="Age")
    department = fields.Many2one('hr.department', string="Department")
    prescription = fields.Text(string="Prescription")

    @api.onchange('token_no')
    def _onchange_token_no(self):
        self.write({
            'patient': self.token_no.patient,
            'doctor': self.token_no.doctor,
            'age': self.token_no.age,
            'department' : self.token_no.department
        })
