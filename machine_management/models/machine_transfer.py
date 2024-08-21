# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MachineTransfer(models.Model):
    _name = "machine.transfer"
    _description = "Machine Transfer"
    _rec_name = 'machine_id'

    machine_id = fields.Many2one('machine.management', 'Machine', required=True, help="Name of the machine")
    serial_no = fields.Char('Serial no', help="Unique serial number of the machine")
    transfer_date = fields.Date('Transfer date', help="Transferring date")
    transfer_type = fields.Selection([('install', 'Install'), ('remove', 'Remove')], required=True,
                                     help="Type of transfer")
    customer_id = fields.Many2one('res.partner', 'Customer', help="Customer who bought the machine")
    internal_notes = fields.Html('Internal notes')
    alternate_ids = fields.Many2many('machine.management', compute='compute_alternate_ids')

    # auto getting serial_no
    @api.onchange('machine_id')
    def _onchange_machine_id(self):
        self.write({
            'serial_no': self.machine_id.serial_no,
        })

    # updating values in machine.management
    def action_add_transfer(self):
        self.machine_id.write({
            'customer_id': self.customer_id.id,
            'state': 'in_service',
        })

    # dynamic domain
    @api.depends('transfer_type')
    def compute_alternate_ids(self):
        for rec in self:
            if rec.transfer_type == 'remove':
                rec.alternate_ids = rec.env['machine.management'].search([('state', '=', 'in_service')])
            elif rec.transfer_type == 'install':
                rec.alternate_ids = rec.env['machine.management'].search([('state', '=', 'active')])
            else:
                rec.alternate_ids = rec.env['machine.management'].search([])
