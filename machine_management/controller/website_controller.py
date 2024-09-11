from odoo.http import request, Controller, route


class WebFormController(Controller):
    @route('/webform', auth='public', website=True)
    def web_form(self, **kwargs):
        return request.render('machine_management.web_form_template')

    @route('/webform/submit', type='http', auth='public', website=True, methods=['POST'])
    def web_form_submit(self, **post):
        request.env['machine.service'].sudo().create({
            'customer_id': request.uid,
            'machine_id': post.get('machine_id'),
            'service_frequency': post.get('service_frequency'),
            'last_service_date': post.get('last_service_date'),
            'state':'request',
        })
        return request.redirect('/service-thank-you')





