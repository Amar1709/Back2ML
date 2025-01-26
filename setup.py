from typing import List
from setuptools import find_packages, setup


def get_requirements(
    file_path: str = 'requirements.txt'
) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    HYPHEN_E_DOT = '-e .'
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='Back2ML',
    version='0.0.1',
    author='Amar',
    author_email='amarparam1709@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
