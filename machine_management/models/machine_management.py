from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MachineManagement(models.Model):
    _name = "machine.management"
    _description = "Machine Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True)
    date_of_purchase = fields.Date('Date')
    purchase_value = fields.Float('Purchase value')
    customer = fields.Char('Customer', readonly=True)
    description = fields.Text('Description')
    warranty = fields.Boolean('Warranty')
    machine_instructions = fields.Html('Machine instructions')
    image = fields.Image('image', )
    serial_no = fields.Char('Serial no')
    sequence_no = fields.Char("Sequence no", default=lambda self: _('New'),
                              copy=False, readonly=True, tracking=True)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)
    machine_type_id = fields.Many2one('machine.type', 'Machine Type')
    transfer_count = fields.Integer(compute='compute_count')
    machine_tag_id = fields.Many2many('machine.tag', string='Machine Tag')
    color = fields.Integer('Color Index', default=0)

    #  smart button
    def get_transfers(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transfer',
            'view_mode': 'tree',
            'res_model': 'machine.transfer',
            'domain': [('machine_id', '=', self.id)],
            'context': "{'create': False}"
        }

    # computing count of transfers
    def compute_count(self):
        for record in self:
            record.transfer_count = self.env['machine.transfer'].search_count([('machine_id', '=', self.id)])

    # state bar
    state = fields.Selection(selection=[
        ('active', 'Active'),
        ('in_service', 'In service'),
    ], string='Status', required=True, copy=False,
        tracking=True, default='active')

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
        for rec in self:
            if rec.purchase_value < 1:
                raise ValidationError("Purchase value must be a positive number")

    # making serial number unique
    @api.constrains('serial_no')
    def _check_registration_no(self):
        for rec in self:
            domain = [('serial_no', '=', rec.serial_no)]
            count = self.sudo().search_count(domain)
            if count > 1:
                raise ValidationError(_("The Serial number should be unique"))

    # button to navigate to machine.transfer
    def transfer_machine_button(self):
        return {
            # 'name': 'machine_management',
            'res_model': 'machine.transfer',
            'type': 'ir.actions.act_window',
            # 'view_type': 'tree',
            'view_mode': 'form',
            # 'view_id': False,
            'context': {'default_machine_id': self.id},
            # 'target': 'current'
        }
