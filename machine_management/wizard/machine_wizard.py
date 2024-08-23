from odoo import fields, models, _
class WhatsappSendMessage(models.TransientModel):
   """This model is used for sending WhatsApp messages through Odoo."""
   _name = 'machine.wizard'
   _description = "Machine Wizard"

   # def action_wizard(self):
   #    return {'type': 'ir.actions.act_window',
   #            'name': _('Warning'),
   #            'res_model': 'machine.wizard',
   #            'view_mode': 'form',
   #            'view_type': 'form',
   #            'context': {},
   #            'target': 'new',
   #            }