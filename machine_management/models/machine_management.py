# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MachineManagement(models.Model):
    _name = "machine.management"
    _description = "Machine Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True, help="name of the machine")
    purchase_value = fields.Float('Purchase value', help="Purchase value of the machine")
    customer_id = fields.Many2one('res.partner', 'Customer', help="The value of machine when purchased", )
    description = fields.Text('Description')
    warranty = fields.Boolean('Warranty', help="Is any warranty for machine")
    machine_instructions = fields.Html('Machine instructions')
    image = fields.Image('image', help="Image of the machine")
    state = fields.Selection(selection=[
        ('active', 'Active'),
        ('in_service', 'In service'),
    ], string='Status', required=True, copy=False,
        tracking=True, default='active')
    serial_no = fields.Char('Serial no', help="Unique serial number for machine")
    sequence_no = fields.Char("Sequence no", default=lambda self: _("New"),
                              copy=False, readonly=True, tracking=True)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company, help="Company name")
    machine_type_id = fields.Many2one('machine.type', 'Machine Type', help="Which is the type of the machine")
    transfer_count = fields.Integer(compute='compute_count_of_transfer')
    service_count = fields.Integer(compute='compute_count_of_service')
    machine_tag_ids = fields.Many2many('machine.tag', string='Machine Tag', help="Machine tags")
    machine_part_id = fields.One2many('machine.part', 'machine_id', 'Machine Parts', help="Parts used for machine")
    date_of_purchase = fields.Date('Purchase date', help="Purchase date of machine")
    today_date = fields.Date(default=fields.date.today())
    total_days = fields.Integer('Age (Days)', help="Age of the machine")
    active = fields.Boolean(default=True)

    # Finding the age of the machine
    @api.onchange('date_of_purchase')
    def onchange_calculate_date(self):
        if self.date_of_purchase and self.today_date:
            purchase_date = datetime.strptime(str(self.date_of_purchase), '%Y-%m-%d')
            today_date = datetime.strptime(str(self.today_date), '%Y-%m-%d')
            self.total_days = (today_date - purchase_date).days

    #  smart button for transfers
    def action_get_transfers(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transfer',
            'view_mode': 'tree,form',
            'res_model': 'machine.transfer',
            'domain': [('machine_id', '=', self.id)],
            'context': "{'create': False}"
        }

    # computing count of transfers
    def compute_count_of_transfer(self):
        self.transfer_count = self.env['machine.transfer'].search_count([('machine_id', '=', self.id)])

    # code for sequence number
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sequence_no', _('New')) == _('New'):
                vals['sequence_no'] = self.env['ir.sequence'].next_by_code('machine.management')
        return super().create(vals_list)

    # making purchase value positive
    @api.constrains('purchase_value')
    def check_negative_number(self):
        if self.purchase_value < 1:
            raise ValidationError("Purchase value must be a positive number")

    # making serial number unique
    @api.constrains('serial_no')
    def check_registration_no(self):
        domain = [('serial_no', '=', self.serial_no)]
        count = self.search_count(domain)
        if count > 1:
            raise ValidationError(_("The Serial number should be unique"))

    # button to navigate to machine.transfer
    def action_transfer_machine_button(self):
        return {
            'name': 'Machine Transfer',
            'res_model': 'machine.transfer',
            'type': 'ir.actions.act_window',
            'view_type': 'tree,form',
            'view_mode': 'form',
            'context': {'default_machine_id': self.id},
            'target': 'current'
        }

    # button to navigate to machine.service
    def action_create_service_button(self):
        return {
            'name': 'Machine Service',
            'res_model': 'machine.service',
            'type': 'ir.actions.act_window',
            'view_type': 'tree,form',
            'view_mode': 'form',
            'context': {'default_machine_id': self.id},
            'target': 'current'
        }

    # smart button for services
    def action_get_service(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Services',
            'view_mode': 'tree,form',
            'res_model': 'machine.service',
            'domain': [('machine_id', '=', self.id)],
            'context': "{'create': False}"
        }

    # computing count of services
    def compute_count_of_service(self):
        self.service_count = self.env['machine.service'].search_count([('machine_id', '=', self.id)])

    # # on delete function for machine
    @api.ondelete(at_uninstall=False)
    def ondelete_machine(self):
        if self.transfer_count > 0 or self.service_count > 0:
            raise ValidationError("You can't delete a machine when there is a transfer or  a service ")
