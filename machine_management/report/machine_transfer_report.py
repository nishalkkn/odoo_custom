from odoo import models, api
from odoo.exceptions import ValidationError


class MachineTransferReport(models.AbstractModel):
    _name = "report.machine_management.machine_transfer_report"

    @api.model
    def _get_report_values(self, docids, data=None):
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
        report = self._cr.fetchall()

        if len(report) == 0:
            raise ValidationError("There is nothing to print")

        return {
            'report': report
        }
