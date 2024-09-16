from odoo import http
from odoo.http import request


class MachineList(http.Controller):
    @http.route('/machine/list', type='json', auth='public')
    def machine_list(self):
        machines = request.env['machine.management'].search([], order = 'id desc', limit=4  )
        machine_data_list = []
        for machine in machines:
            image = '/web/image/%s/%s/image' % (machine._name, machine.id)
            machine_data = {
                'machine': machine.name,
                'image':image
            }
            machine_data_list.append(machine_data)
        data_list = {
            'data': machine_data_list
        }
        res = http.Response(template='machine_management.machine_list',
                            qcontext=data_list)

        # print('machine_data_list',machine_data_list)
        # print('data_list',data_list)
        # print('res',res)
        return res.render()
