from odoo import models, fields, api, _


class MachineManagement(models.Model):
    _name = "machine.management"
    _description = "Machine Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    product = fields.Char('Name', required=True)
    date_of_purchase = fields.Date('Date')
    purchase_value = fields.Integer('Purchase value')
    customer = fields.Char('Customer', required=True)
    description = fields.Text('Description')
    warranty = fields.Boolean('Warranty')
    machine_instructions = fields.Html('Machine instructions')
    image = fields.Image('image', )
    serial_no = fields.Char('Serial no')
    name = fields.Char('name')
    # state bar
    state = fields.Selection(selection=[
        ('active', 'Active'),
        ('in_service', 'In service'),
    ], string='Status', required=True, copy=False,
        tracking=True, default='active')

    # code for sequence number
    @api.model_create_multi
    def create(self, vals_list):
        """ Create a sequence for the hospital op """
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital_op_ticket.reference')
        return super().create(vals_list)