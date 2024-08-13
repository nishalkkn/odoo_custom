from odoo import models, fields, api


class MachineTransfer(models.Model):
    _name = "machine.transfer"
    _description = "Machine Transfer"
    _rec_name = 'machine_id'

    machine_id = fields.Many2one('machine.management', 'Machine', required=True)
    serial_no = fields.Char('Serial no')
    transfer_date = fields.Date('Transfer date')
    transfer_type = fields.Selection([('install', 'Install'), ('remove', 'Remove')], required=True, default="remove")
    customer = fields.Char('Customer')
    internal_notes = fields.Html('Internal notes')

    # auto getting serial_no
    @api.onchange('machine_id')
    def _onchange_machine_id(self):
        self.write({
            'serial_no': self.machine_id.serial_no,
        })

    # updating values in machine.management
    def add_transfer(self):
        self.machine_id.write({
            'customer': self.customer,
            'state': 'in_service'
        })
