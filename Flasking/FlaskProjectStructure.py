# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:51:46 2018

@author: sanooj
"""
"""
|-flasky
    |-app/
        |-templates/
        |-static/
        |-main/
            |-__init__.py
            |-errors.py
            |-forms.py
            |-views.py
        |-__init__.py
        |-email.py
        |-models.py
    |-migrations/
    |-tests/
        |-__init__.py
        |-test*.py
    |-venv/
    |-requirements.txt
    |-config.py
    |-manage.py
"""

#python code to create flask project structure

import os
def create_flasky_flask(path=os.path.expanduser("~"), directory="flasky", 
                        app_name="flask_app"):
    
    #path without including app name
    app_container_dir = \
    os.path.join(path,directory)
    
    #path including app name
    app_dir = \
    os.path.join(app_container_dir,app_name)
    
    directory_full_path = \
    app_dir
    
    def create_dir_at_path(relative_path=None):
        
        full_path = \
        directory_full_path if relative_path is None else os.path.join(
                directory_full_path,
                relative_path
                )
        
        if not os.path.exists(full_path):
            os.makedirs(full_path)
    
# =============================================================================
#     #creates
#     |-flasky
#     |-app/    
# =============================================================================
                
    create_dir_at_path(directory_full_path)
    
# =============================================================================
#      |-__init__.py
#      |-email.py
#      |-models.py
# =============================================================================
    for file_name in ["__init__.py" , "email.py", "models.py"]:
        
        full_file_path = \
        os.path.join(directory_full_path,file_name)
        
        open(full_file_path,"a").close()
    
# =============================================================================
#         |-templates/
#         |-static/
#         |-main/ 
# =============================================================================
    for directory in ["templates" , "static", "main"]:
        
        directory_full_path = \
        os.path.join(app_dir,directory)
        
        create_dir_at_path(directory_full_path)
    
# =============================================================================
#             |-__init__.py
#             |-errors.py
#             |-forms.py
#             |-views.py    
# =============================================================================
    for file_name in ["__init__.py" , "errors.py", "forms.py", "views.py"]:
        
        full_file_path = \
        os.path.join(app_dir,"main",file_name)
        
        open(full_file_path,"a").close()

# =============================================================================
#     |-migrations/
#     |-tests/    
# =============================================================================
    for directory in ["migrations" , "tests"]:
        
        directory_full_path = \
        os.path.join(app_container_dir,directory)
        
        create_dir_at_path(directory_full_path)
        
# =============================================================================
#           |-__init__.py
#           |-test*.py
# =============================================================================
    for file_name in ["__init__.py" , "test.py"]:
        
        full_file_path = \
        os.path.join(app_container_dir,"tests",file_name)
        
        open(full_file_path,"a").close()
        
# =============================================================================
#   |-venv/
# =============================================================================
        directory_full_path = \
        os.path.join(app_container_dir,"venv")
        
        create_dir_at_path(directory_full_path)

# =============================================================================
#   |-requirements.txt
#   |-config.py
#   |-manage.py
# =============================================================================
    for file_name in ["requirements.txt" , "config.py", "manage.py"]:
        
        full_file_path = \
        os.path.join(app_container_dir,file_name)
        
        open(full_file_path,"a").close()
        
create_flasky_flask()