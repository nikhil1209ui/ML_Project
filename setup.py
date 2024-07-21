from setuptools import find_packages,setup
from typing import List

HYPHEN_E = '-e .'

def get_requirements(File_path:str)->List[str]:
    '''
    this function will return the list of requirements
    
     '''
    requirements =[]

    with open(File_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('/n'," ")for req in requirements]
    
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
            
    return requirements




setup(
name = 'mlproject',
version = '0.0.1',
author = 'NIKHIL',
author_email = 'nikhilez1207@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirement.txt')
)