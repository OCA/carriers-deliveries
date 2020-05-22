# Copyright 2020 Trey, Kilobytes de Soluciones
# Copyright 2020 FactorLibre
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Delivery State',
    'summary': 'Provides fields to be able to contemplate the tracking states'
               'and also adds a global fields',
    'author': 'Trey (www.trey.es), '
              'FactorLibre, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/delivery-carrier',
    'license': 'AGPL-3',
    'category': 'Delivery',
    'version': '12.0.1.0.0',
    'depends': [
        'delivery',
    ],
    'data': [
        'views/stock_picking_views.xml',
    ],
}
