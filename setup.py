from setuptools import setup, find_packages,setup 
from typing import List
def get_requirement(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements =[req.replace('\n', '') for req in requirements]
        return requirements






setup(    
    name='project',
    version='0.1.0',
    packages=find_packages(),
    author='Appy',
    install_requires=get_requirement('requirements.txt')
)
