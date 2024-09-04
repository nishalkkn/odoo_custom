from odoo import models, fields


class ToleranceWizard(models.TransientModel):
    """This model is used for creating a wizard when exceeding tolerance."""
    _name = 'tolerance.wizard'
    _description = "Tolerance Wizard"

    stock_picking_id = fields.Many2one('stock.picking')


    def action_continue(self):
        """continue button in wizard"""
        print(self.stock_picking_id.state)
        self.stock_picking_id.write({
            'state':'done',
        })
