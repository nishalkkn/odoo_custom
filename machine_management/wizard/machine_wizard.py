import io
import json

import xlsxwriter

from odoo import fields, models
from odoo.tools import date_utils
from odoo.exceptions import ValidationError


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
                'model': 'machine.wizard',
                'options': json.dumps(data, default=date_utils.json_default),
                'output_format': 'xlsx',
                'report_name': 'Machine Transfer Excel Report',
            },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        query = """select
                   machine_management.name as machine,
                   machine_transfer.transfer_date as date,
                   machine_transfer.transfer_type as transfer_type,
                   res_partner.name as customer
                   from machine_transfer
                   inner join machine_management on machine_transfer.machine_id = machine_management.id
                   left join res_partner on  machine_transfer.customer_id = res_partner.id
                   where 1=1"""

        if data['machine_id']:
            query += """ and machine_management.id = %s """ % data['machine_id']
        if data['from_date']:
            query += """ and machine_transfer.transfer_date >= '%s' """ % data['from_date']
        if data['to_date']:
            query += """ and machine_transfer.transfer_date <= '%s' """ % data['to_date']
        if data['transfer_type']:
            query += """ and machine_transfer.transfer_type = '%s' """ % data['transfer_type']
        if data['customer_id']:
            query += """ and res_partner.id = %s """ % data['customer_id']

        self._cr.execute(query)
        report = self._cr.dictfetchall()

        if len(report) == 0:
            raise ValidationError("There is nothing to print")

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()

        cell_format = workbook.add_format({'font_size': '12px', 'align': 'center'})
        head = workbook.add_format({'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '12px', 'align': 'center', 'bold': True})

        sheet.merge_range('B2:I3', 'Machine Transfer Report', head)
        sheet.merge_range('C5:D5', "Machine", txt)
        sheet.merge_range('E5:F5', "Transfer date", txt)
        sheet.merge_range('G5:H5', "Transfer type", txt)
        sheet.merge_range('I5:J5', "Customer", txt)
        for i, report in enumerate(report, start=6):
            sheet.merge_range(f'C{i}:D{i}', report['machine'], cell_format)
            sheet.merge_range(f'E{i}:F{i}', report['date'].strftime('%d-%m-%Y'), cell_format)
            sheet.merge_range(f'G{i}:H{i}', report['transfer_type'], cell_format)
            sheet.merge_range(f'I{i}:J{i}', report['customer'], cell_format)
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
