# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, Command
from odoo.exceptions import ValidationError


class MachineService(models.Model):
    _name = 'machine.service'
    _description = 'Machine Service'
    _rec_name = 'machine_id'

    machine_id  = fields.Many2one('machine.management', 'Machine', required=True, help="Name of the machine")
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
    ], string='State', required=True, copy=False, tracking=True, default='open', store=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company,
                                 help="Name of the company")
    parts_ids = fields.Many2many('machine.part', 'machine_id')
    alternate_part_ids = fields.Many2many('machine.part', compute='_compute_parts_consumed')
    invoice_ids = fields.One2many('account.move', 'service_id', 'Invoice id')
    invoice_count = fields.Integer('Invoice count', compute='_compute_count_of_transfer')
    service_frequency = fields.Selection([('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')],
                                         'Service frequency', required=True, help="Service frequency")
    last_service_date = fields.Date('Last service date', help="Date of last service")
    next_service_date = fields.Date('Next service date', help="Date of next service",
                                    compute='_compute_next_service_date')

    # c=fields.Integer()

    @api.depends('machine_id')
    def _compute_parts_consumed(self):
        """filter parts_consumed wrt machine_id"""
        for rec in self:
            rec.alternate_part_ids = self.env['machine.part'].search([('machine_id', '=', self.machine_id.id)])

    def action_start_case(self):
        """button to change state to started """
        self.write({
            'state': 'started'
        })

    def action_close_case(self):
        """button to change state to done and send email to customer when state become done """
        template = self.env.ref('machine_management.email_template_name')
        template.send_mail(self.id, force_send=True)

        self.write({
            'state': 'done'
        })

    def action_get_invoices(self):
        """smart button for invoice"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('service_id', '=', self.id)],
            'context': "{'create': False}",
        }

    def _compute_count_of_transfer(self):
        """computing count of invoices"""
        for rec in self:
            rec.invoice_count = self.env['account.move'].search_count([('service_id', '=', self.id)])

    @api.onchange('machine_id')
    def onchange_machin_id(self):
        """onchange machin_id"""
        self.write({
            'customer_id': self.machine_id.customer_id
        })

    def action_create_invoice(self):
        """creating invoice"""
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
                'invoice_line_ids': invoice_line,
                'service_id': self.id,
            })

            return {
                'name': 'customer invoice',
                'res_model': 'account.move',
                'type': 'ir.actions.act_window',
                'view_type': 'tree,form',
                'view_mode': 'form',
                'target': 'current',
                'res_id': existing_invoice.id,
            }

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.customer_id.id,
            'invoice_line_ids': invoice_line,
            'service_id': self.id,
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

    @api.constrains('machine_id')
    def check_machine_id(self):
        """check the machine_id it there any service for same machine"""
        service_count = self.env['machine.service'].search_count(
            [('machine_id', '=', self.machine_id.id), ('state', '!=', 'done')])
        if service_count > 1:
            raise ValidationError("This machine already has a service")

    @api.depends('last_service_date', 'service_frequency')
    def _compute_next_service_date(self):
        """computing next service date"""
        for rec in self:
            rec.next_service_date=False
            if rec.last_service_date:
                if rec.service_frequency == 'weekly':
                    rec.next_service_date = rec.last_service_date + relativedelta(weeks=1)
                elif rec.service_frequency == 'monthly':
                    rec.next_service_date = rec.last_service_date + relativedelta(months=1)
                else:
                    rec.next_service_date = rec.last_service_date + relativedelta(years=1)


    def recurring_service(self):
        print(self)
        all_recs = self.search([])
        for rec in all_recs:
            print(rec.next_service_date)
