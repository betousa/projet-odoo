{
    'name': 'Gestion des tâches simples',
    'version': '1.0',
    'summary': 'Gestion des tâches sans workflow',
    'description': 'Module Odoo pour gérer des tâches simples',
    'category': 'Productivité',
    'author': 'Boutaina',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
    'application': True,
}
