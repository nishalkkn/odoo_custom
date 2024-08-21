# -*- coding: utf-8 -*-
from odoo import models, fields, api, Command


class MachineService(models.Model):
    _name = 'machine.service'
    _description = 'Machine Service'
    _rec_name = 'machine_id'

    machine_id = fields.Many2one('machine.management', 'Machine', required=True, help="Name of the machine")
    customer_id = fields.Many2one('res.partner', 'Customer', help="Name of the customer")
    date_of_service = fields.Date('Date of service', help="Date of the service")
    description = fields.Text('Description')
    internal_note = fields.Html('Internal note')
    tech_person_ids = fields.Many2many('hr.employee', string='Tech person', help="Assigned person for the service")
    state = fields.Selection(selection=[
        ('open', 'Open'),
        ('started', 'Started'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='State', required=True, copy=False, tracking=True, default='open')
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company,
                                 help="Name of the company")
    parts_ids = fields.Many2many('machine.part', 'machine_id')
    alternate_part_ids = fields.Many2many('machine.part', compute='compute_parts_consumed')

    # making parts_consumed wrt machine_id
    @api.depends('machine_id')
    def compute_parts_consumed(self):
        self.alternate_part_ids = self.env['machine.part'].search([('machine_id', '=', self.machine_id.id)])

    # button to start the case
    def action_start_case(self):
        self.write({
            'state': 'started'
        })

    # button to close the case
    def action_close_case(self):
        self.write({
            'state': 'done'
        })

    # onchange machin_id
    @api.onchange('machine_id')
    def onchange_machin_id(self):
        self.write({
            'customer_id': self.machine_id.customer_id
        })

    # creating invoice
    def action_create_invoice(self):
        existing_invoice = self.env['account.move'].search([
            ('move_type', '=', 'out_invoice'),
            ('partner_id', '=', self.customer_id.id),
            ('state', '=', 'draft')
        ], limit=1)

        invoice_line = [
                           Command.create({
                               'product_id': rec.product_id.id,
                               'quantity': rec.quantity,
                           }) for rec in self.parts_ids
                       ] + [
                           Command.create({
                               'product_id': self.env.ref('machine_management.product_product_3').id,
                               'quantity': 1,
                           })
                       ]
        if existing_invoice:
            existing_invoice.write({
                'invoice_line_ids': invoice_line
            })

            return {
                'name': 'customer invoice',
                'res_model': 'account.move',
                'type': 'ir.actions.act_window',
                'view_type': 'tree,form',
                'view_mode': 'form',
                'target': 'current',
                'res_id': existing_invoice.id
            }

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.customer_id.id,
            'invoice_line_ids': invoice_line,
        })

        return {
            'name': 'customer invoice',
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'view_type': 'tree,form',
            'view_mode': 'form',
            'target': 'current',
            'res_id': invoice.id,
        }
