import json

from odoo import fields, models
from odoo.tools import date_utils


class CreateReportWizard(models.TransientModel):
    _name = 'machine.wizard'
    _description = "Machine Wizard"

    machine_id = fields.Many2one('machine.management', 'Machine')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    customer_id = fields.Many2one('res.partner', 'Customer')
    transfer_type = fields.Selection([('install', 'Install'), ('remove', 'Remove')], 'Transfer type')

    def action_print_record(self):
        """print pdf button in wizard"""
        data = {
            'machine_id': self.machine_id.id,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'customer_id': self.customer_id.id,
            'transfer_type': self.transfer_type
        }
        return self.env.ref('machine_management.action_report_machine_transfer').report_action(None, data=data)

    def action_print_exel(self):
        """print exel button in wizard"""
        data = {
            'machine_id': self.machine_id.id,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'customer_id': self.customer_id.id,
            'transfer_type': self.transfer_type
        }
        return {
            'type': 'ir.actions.report',
            'data': {
                'model': 'report.machine_management.machine_transfer_report',
                'options': json.dumps(data, default=date_utils.json_default),
                'output_format': 'xlsx',
                'report_name': 'Machine Transfer Excel Report',
            },
            'report_type': 'xlsx',
        }
