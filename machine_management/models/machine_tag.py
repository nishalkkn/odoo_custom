from odoo import models, fields


class MachineTag(models.Model):
    _name = "machine.tag"
    _description = "Machine Tags"

    name = fields.Char('Tag')
    color=fields.Integer('Color')
