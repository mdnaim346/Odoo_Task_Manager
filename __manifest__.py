# -*- coding: utf-8 -*-
{
    'name' : 'Task_Manager',
    'version' : '1.2',
    'sequence': 10,
    'summary': 'Simple Task Management Module',
    'description': """
Task Manager for Odoo 17
=======================
This module allows users to track and manage their daily tasks.
    """,
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
        
    ],
    
    'installable': True,
    'application': True,
   
    'assets': {
       
        'web.assets_backend': [
            
            
        ],
        'web.assets_frontend': [
           
        ],
        
    },
    
}
