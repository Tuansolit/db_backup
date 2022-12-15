{
    'name': "db_backup",
    'summary': "Manage books easily",
    'description': """
Manage Library
==============
Description related to library.
""",
    'author': "Your name",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '15.0.13.0.1.0.1',
    'depends': ['base', 'account', 'sale', 'sale_management', 'product', 'mail', 'hr', 'crm', 'sale_crm'],
    'data': ['security/ir.model.access.csv',
             'views/db_backup_view.xml',
             'views/res_config_settings.xml',
             'data/ir_cron_data.xml'
             ],
    'demo': ['data/demo.xml'],
}
