from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'


#Making a function for reading all the packages present in requirements file
def get_requirements(filepath:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()  #this will read the every line present in requirements.txt but also give \n with that so for replacing \n with empty space we use the below line
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    
    return requirements
setup(
    name="MLProject",
    version="0.0.1",
    author="Vaishnavi Pandey",
    author_email="vaishpandey02@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
)