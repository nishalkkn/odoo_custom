from odoo import http


class ElearningSnippet(http.Controller):
    @http.route(['/latest_elearning_courses'], type="json", auth="public", website=True, methods=['POST'])
    def all_courses(self):
        courses = http.request.env['machine.management'].search_read(['name', 'image', 'id'],order='id desc', limit=10)
        return courses
