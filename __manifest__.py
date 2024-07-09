{
    'name': 'Tonata Test',
    'version': '1.1',
    'sequence': 1,
    'description': "Create checking before saving values on res.partner models",
    'depends': [
        # 'base',
          'account',
        # 'sale_management'
        # 'base_accounting_kit',
        # 'point_of_sale'

    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/business_model_data.xml',
        # 'views/sale.xml',
        # 'views/account.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}