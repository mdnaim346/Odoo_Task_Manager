from odoo import models, fields

class Task(models.Model):
    _name="task.manager"
    _description="Task Manager"

    name= fields.Char(string="Task Name",required = True)
    description=fields.Text(string="Description")
    is_done= fields.Boolean(string="Is Done",default=False)