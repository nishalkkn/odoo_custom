from odoo import models, fields, api


class MachineService(models.Model):
    _name = 'machine.service'
    _description = 'Machine Service'
    _rec_name = 'machine_id'

    machine_id = fields.Many2one('machine.management', 'Machine', required=True)
    customer_id = fields.Many2one('res.partner', 'Customer')
    date_of_service = fields.Date('Date of service')
    description = fields.Text('Description')
    internal_note = fields.Html('Internal note')
    tech_person_id = fields.Many2many('hr.employee', string='Tech person')
    state = fields.Selection(selection=[
        ('open', 'Open'),
        ('started', 'Started'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='State', required=True, copy=False, tracking=True, default='open')
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company)
    parts_id = fields.Many2many('machine.part', 'machine_id')
    alternate_parts = fields.Many2many('machine.part',compute='compute_parts_consumed')

    # making parts_consumed wrt machine_id
    @api.depends('machine_id')
    def compute_parts_consumed(self):
        self.alternate_parts = self.env['machine.part'].search([('machine_id', '=', self.machine_id.id)])

    # button to start the case
    def start_case(self):
        self.write({
            'state':'started'
        })

    # button to close the case
    def close_case(self):
        self.write({
            'state':'done'
        })

    def create_invoice(self):
        return {
            'name': 'Invoice',
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'view_type': 'tree,form',
            'view_mode': 'form',
            'context': {},
            'target': 'current'
        }



