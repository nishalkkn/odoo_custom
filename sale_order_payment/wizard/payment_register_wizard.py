# from odoo import models, fields, _, api
# from odoo.exceptions import UserError
#
#
# class PaymentRegisterWizard(models.TransientModel):
#     _inherit = 'account.payment.register'
#
#
#     @api.model
#     def default_get(self, fields_list):
#         # OVERRIDE
#         res = super(PaymentRegisterWizard, self).default_get(fields_list)
#
#         if 'line_ids' in fields_list and 'line_ids' not in res:
#
#             # Retrieve moves to pay from the context.
#
#             if self._context.get('active_model') == 'account.move':
#                 lines = self.env['account.move'].browse(self._context.get('active_ids', [])).line_ids
#             elif self._context.get('active_model') == 'account.move.line':
#                 lines = self.env['account.move.line'].browse(self._context.get('active_ids', []))
#
#
#             elif self._context.get('active_model') == 'sale.order':
#                 lines = self.env['sale.order'].browse(self._context.get('active_ids', []))
#
#
#             else:
#                 raise UserError(_(
#                     "The register payment wizard should only be called on account.move or account.move.line records."
#                 ))
#
#             if 'journal_id' in res and not self.env['account.journal'].browse(res['journal_id']).filtered_domain([
#                 *self.env['account.journal']._check_company_domain(lines.company_id),
#                 ('type', 'in', ('bank', 'cash')),
#             ]):
#                 # default can be inherited from the list view, should be computed instead
#                 del res['journal_id']
#
#             # Keep lines having a residual amount to pay.
#             available_lines = self.env['account.move.line']
#             valid_account_types = self.env['account.payment']._get_valid_payment_account_types()
#             for line in lines:
#                 if line.move_id.state != 'posted':
#                     raise UserError(_("You can only register payment for posted journal entries."))
#
#                 if line.account_type not in valid_account_types:
#                     continue
#                 if line.currency_id:
#                     if line.currency_id.is_zero(line.amount_residual_currency):
#                         continue
#                 else:
#                     if line.company_currency_id.is_zero(line.amount_residual):
#                         continue
#                 available_lines |= line
#
#             # Check.
#             if not available_lines:
#                 raise UserError(_("You can't register a payment because there is nothing left to pay on the selected journal items."))
#             if len(lines.company_id.root_id) > 1:
#                 raise UserError(_("You can't create payments for entries belonging to different companies."))
#             if len(set(available_lines.mapped('account_type'))) > 1:
#                 raise UserError(_("You can't register payments for both inbound and outbound moves at the same time."))
#
#             res['line_ids'] = [(fields.Command.set(available_lines.ids))]
#
#         return res
#
#     # return super(className, self)._cart_update(self)
#
