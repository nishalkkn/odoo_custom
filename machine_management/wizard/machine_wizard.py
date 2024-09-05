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
        # print('report = ', report)

        query = """select machine_management.name,machine_transfer.transfer_date,machine_transfer.transfer_type,res_partner.name 
        from machine_transfer 
        inner join machine_management on machine_transfer.machine_id = machine_management.id
        inner join res_partner on  machine_transfer.customer_id = res_partner.id
        where  machine_management.id= %s """ % self.machine_id.id
        self._cr.execute(query)
        report = self._cr.fetchall()
        print('report = ', report)
        data = {'date': self.read()[0], 'report': report}
        return self.env.ref('machine_management.action_report_machine_transfer').report_action(None, data=data)


    # def action_report_truck_booking(self):
    #    query = """select pr.name,fv.name as truck,
    #               gt.name as goods,
    #               tb.from_location,
    #               tb.to_location,
    #               tb.distance,
    #            tb.weight,tb.unit,amount,tb.date,tb.state from truck_booking as tb
    #            inner join res_partner as pr on pr.id = tb.partner_id
    #            inner join fleet_vehicle_model as fv on fv.id = tb.truck_id
    #            inner join goods_type as gt on gt.id = tb.goods_type_id """
    #
    #    if self.from_date:
    #        query += """ where tb.date >= '%s' and tb.date <= '%s'""" % self.from_date, %self.to_date
    #     self.env.cr.execute(query)
    #     report = self.env.cr.dictfetchall()
    #     data = {'date': self.read()[0], 'report': report}
    #     return self.env.ref('module_name.action_report_booking').report_action(None, data=data)
