"""
The setup.py file is an essential part of packing and 
distributing python projects. It is used by setuptools
(or distutils in older python versions) to define the configuration
of you projects, such as its metadata dependencies, and more
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the lines
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                # ignore empyt lines and -e .
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements .txt file not found!!")

    return requirements_lst

setup (
    name = "NetworkSecurity",
    version= "0.0.1",
    author= "Vishal Rewaskar",
    author_email= "vishalrewaskar@outlook.com",
    packages= find_packages(),
    install_requires = get_requirements()
)