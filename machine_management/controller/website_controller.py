import base64

from odoo import Command
from odoo.http import Controller, route
from odoo.http import request


class WebFormController(Controller):
    @route('/webform', auth='public', website=True)
    def web_form(self, **kwargs):
        return request.render('machine_management.web_form_template')

    @route('/webform/submit', type='http', auth='public', website=True, methods=['POST'])
    def web_form_submit(self, **post):
        attachment = request.env['ir.attachment']
        files = request.httprequest.files.getlist('image')
        machine_service = request.env['machine.service'].sudo().create({
            'customer_id': request.uid,
            'machine_id': post.get('machine_id'),
            'service_frequency': post.get('service_frequency'),
            'last_service_date': post.get('last_service_date'),
            'state': 'request',
        })
        for file in files:
            attachment_id = attachment.create({
                'name': file.filename,
                'type': 'binary',
                'datas': base64.b64encode(file.read()),
            })
            print('attachment', attachment_id)
            machine_service.write({
                'attachment_ids': [Command.link(attachment_id.id)]
            })
        return request.redirect('/service-thank-you')

        # image = post.get('image')
        # image_base64 = False
        # if image:
        #     image_base64 = base64.b64encode(image.read())
        #
        # request.env['machine.service'].sudo().create({
        #     'customer_id': request.env.user.id,
        #     'machine_id': post.get('machine_id'),
        #     'service_frequency': post.get('service_frequency'),
        #     'last_service_date': post.get('last_service_date'),
        #     'image': image_base64,
        #     'state': 'request',
        # })
        # return request.redirect('/service-thank-you')

        # images = request.httprequest.files.getlist('image')
        # image_list = []
        # for image in images:
        #     if image:
        #         image_base64 = base64.b64encode(image.read())
        #         image_list.append(image_base64)
