from odoo import models, fields

class Task(models.Model):
    _name="task.manager"
    _description="Task Manager"

    name= fields.Char(string="Task Name",required = True)
    description=fields.Text(string="Description")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done')
    ], string="Status", default='pending')


    def action_mark_done(self):
     for task in self:
        task.status = 'done'