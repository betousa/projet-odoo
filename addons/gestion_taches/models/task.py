from odoo import models, fields

class Task(models.Model):
    _name = 'gestion.tache'
    _description = 'Tâche'

    name = fields.Char(string="Nom de la tâche", required=True)
    description = fields.Text(string="Description")
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    responsable = fields.Many2one('res.users', string="Responsable")
    priorite = fields.Selection([
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute')
    ], string="Priorité", default='moyenne')
