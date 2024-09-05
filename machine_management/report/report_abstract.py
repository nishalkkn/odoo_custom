from odoo import models, api


class MachineTransferReport(models.AbstractModel):
    _name = "report.machine_management.machine_transfer_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        print("hello world")
        query = """select machine_management.name as machine,machine_transfer.transfer_date as date,machine_transfer.transfer_type as transfer_type,res_partner.name as customer    
                from machine_transfer
                inner join machine_management on machine_transfer.machine_id = machine_management.id
                inner join res_partner on  machine_transfer.customer_id = res_partner.id"""
        self._cr.execute(query)
        report = self._cr.fetchall()
        return {
            'doc_model': 'machine.transfer',
            'report':report
        }
