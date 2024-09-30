
from setuptools import setup,find_packages
from typing import List


remover = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    this fucntion is used for getting  the list of 
     requirements

    """
    requirements =[]
    with open(file_path,"r") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if remover in requirements:
            requirements.remove(remover)
    return requirements
          



setup(
    name="E2EMLproject",
    version='0.1',
    author = "Prasanna Kumar",
    author_email="prsnkmrreddy@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)

