from odoo import http
from odoo.http import request


class MachineList(http.Controller):
    @http.route('/machine_lists', type='json', auth='public')
    def machine_list(self):
        machine = request.env['machine.management'].search_read([], ['name', 'image'], order='id desc')
        return machine
