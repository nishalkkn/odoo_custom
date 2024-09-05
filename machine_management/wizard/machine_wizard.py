from odoo import fields, models


class CreateReportWizard(models.TransientModel):
    _name = 'machine.wizard'
    _description = "Machine Wizard"

    machine_id = fields.Many2one('machine.management')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    customer_id = fields.Many2one('res.partner')
    transfer_type = fields.Selection([('install', 'Install'), ('remove', 'Remove')])

    def action_print_record(self):
        # query = """select machine_management.name,machine_transfer.transfer_date,machine_transfer.transfer_type,res_partner.name
        # from machine_transfer
        # inner join machine_management on machine_transfer.machine_id = machine_management.id
        # inner join res_partner on  machine_transfer.customer_id = res_partner.id
        # where  machine_management.id= %s
        # and machine_transfer.transfer_type = %s
        # and machine_transfer.transfer_date between %s and %s
        # and res_partner.id = %s"""
        # self.env.cr.execute(query,
        #                     (self.machine_id.id, self.transfer_type, self.from_date, self.to_date, self.customer_id.id))
        # report = self.env.cr.fetchall()

        data = {
            'machine_id': self.machine_id,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'customer_id':self.customer_id,
            'transfer_type':self.transfer_type
        }
        return self.env.ref('machine_management.action_report_machine_transfer').report_action(None, data=data)
