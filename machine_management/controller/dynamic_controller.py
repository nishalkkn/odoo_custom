from odoo import http
from odoo.http import request
from time import time

class DynamicSnippets(http.Controller):
   """This class is for the getting values for dynamic product snippets
      """
   @http.route('/top_selling_products', type='json', auth='public')
   def top_selling(self):
       """Function for getting the current website,top sold products and
          its categories.
           Return
                 products-most sold products
                 unique_categories-categories of all products
                 current_website-the current website for checking products or
           """
       current_website = request.env['website'].sudo().get_current_website().id
       public_categ_id = request.env[
           'product.public.category'].sudo().search_read([], ['name',
                                                              'website_id'])
       products = []
       public_categories = []
       for category in public_categ_id:
           products_search_read = request.env['product.template'].with_user(
               1).search_read(
               [('is_published', '=', True),
                ('public_categ_ids.id', '=', category['id'])],
               ['name', 'image_1920', 'public_categ_ids', 'website_id',
                'sales_count', 'list_price'], order='sales_count')
           for product in products_search_read:
               if product['sales_count'] != 0:
                   products.append(product)
                   public_categories.append(category)
       unique_categories = [dict(categories) for categories in
                            {tuple(sorted(record.items())) for record in
                             public_categories}]
       products = sorted(products, key=lambda i: i['sales_count'],
                         reverse=True)
       unique_id = "pc-%d" % int(time.time() * 1000)
       return products, unique_categories, current_website, unique_id



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
        return res.render()

