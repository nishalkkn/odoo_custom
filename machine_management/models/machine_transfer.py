from odoo import models, fields, api


class MachineTransfer(models.Model):
    _name = "machine.transfer"
    _description = "Machine Transfer"
    _rec_name = 'machine'

    machine = fields.Many2one('machine.management', 'Machine', required=True)
    serial_no = fields.Char('Serial no')
    transfer_date = fields.Date('Transfer date')
    transfer_type = fields.Selection([('install', 'Install'), ('remove', 'Remove')], required=True, default="remove")
    customer = fields.Char('Customer')
    internal_notes = fields.Html('Internal notes')

    # auto getting serial_no
    @api.onchange('machine')
    def _onchange_machine(self):
        self.write({
            'serial_no': self.machine.serial_no,
        })

    def transfer_history_button(self):
        return {
            # 'name': 'machine_management',
            'res_model': 'machine.transfer',
            'type': 'ir.actions.act_window',
            # 'view_type': 'tree',
            'view_mode': 'tree',
            # 'view_id': False,
            # 'context': {},
            # 'target': 'current'
        }
