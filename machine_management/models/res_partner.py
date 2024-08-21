# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    machine_id = fields.One2many('machine.management', 'customer_id', string="Machine")
    alternative_cust_ids = fields.Many2many('machine.management', compute="compute_employee_machine_count")

    # domain setting for machine_id
    @api.depends('name')
    def compute_employee_machine_count(self):
        self.alternative_cust_ids = self.env['machine.management'].search([('customer_id', '=', self.name)])

    # archiving machine belongs to customer
    def action_archive(self):
        res = super().action_archive()
        machine = self.env['machine.management'].search([('customer_id.id', '=', self.id)])
        machine.write({'active':False})
        return res

    # un-archiving machine belongs to customer
    def action_unarchive(self):
        res = super().action_unarchive()
        machine = self.env['machine.management'].search([('customer_id.id', '=', self.id),('active', '=', False)])
        machine.write({'active': True})
        return res