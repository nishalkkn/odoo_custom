from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MachineTransfer(models.Model):
    _name = "machine.transfer"
    _description = "Machine Transfer"
    _rec_name = 'machine_id'

    machine_id = fields.Many2one('machine.management', 'Machine', required=True)
    serial_no = fields.Char('Serial no')
    transfer_date = fields.Date('Transfer date')
    transfer_type = fields.Selection([('install', 'Install'), ('remove', 'Remove')], required=True)
    customer = fields.Many2one('res.partner', 'Customer')
    internal_notes = fields.Html('Internal notes')
    alternate_ids = fields.Many2many('machine.management', compute='compute_alternate_ids')

    # auto getting serial_no
    @api.onchange('machine_id')
    def _onchange_machine_id(self):
        self.write({
            'serial_no': self.machine_id.serial_no,
        })

    # updating values in machine.management
    def add_transfer(self):
        self.machine_id.write({
            'customer': self.customer.name,
            'state': 'in_service',
        })

    # dynamic domain
    @api.depends('transfer_type')
    def compute_alternate_ids(self):
        if self.transfer_type == 'remove':
            self.alternate_ids = self.env['machine.management'].search([('state', '=', 'in_service')])
        elif self.transfer_type == 'install':
            self.alternate_ids = self.env['machine.management'].search([('state', '=', 'active')])
        else:
            self.alternate_ids = self.env['machine.management'].search([])
