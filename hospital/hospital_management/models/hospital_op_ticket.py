
from odoo import models, fields, api, _


class OpTicket(models.Model):
    _name = "hospital.op.ticket"
    _description = "Op Ticket"

    name = fields.Char('name', default=lambda self: _('New'),
                       copy=False, readonly=True, tracking=True)
    token_no = fields.Integer(string="Token no")
    patient = fields.Many2one('res.partner', required=True, string="Patient")
    doctor = fields.Many2one('hr.employee', required=True, string="Doctor")
    age = fields.Integer(string="Age")
    date = fields.Date(string="Date")
    department = fields.Many2one('hr.department', string="Department")

    # state bar
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')

    # code for sequence number
    @api.model_create_multi
    def create(self, vals_list):
        """ Create a sequence for the hospital op """
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital_op_ticket.reference')
        return super().create(vals_list)

    # code for copy age automatically
    @api.onchange('patient')
    def _onchange_patient(self):
        self.write({
            'age': self.patient.age,
        })

    # code for copy department of doctor
    @api.onchange('doctor')
    def _onchange_doctor(self):
        self.write({
            'department': self.doctor.department_id,
        })

    # state  change on button click
    def button_done(self):
        self.write({
            'state': "done",
        })




