# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Task_Manager',
    'version' : '1.2',
    'sequence': 10,
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
