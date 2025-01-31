from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
        This function returns a list of requirements from a file
    '''
    # requirements = []
    # with open(file_path, 'r') as file_obj:
    #     requirements = [req.replace('\n', '') for req in file_obj]  # Iterate directly over file_obj

    #     if HYPEN_E_DOT in requirements:
    #         requirements.remove(HYPEN_E_DOT)
    # return requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = "mlproject",
    version='0.0.1',
    author='Gopal',
    author_email='geekrootml@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)