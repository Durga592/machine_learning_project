from setuptools import find_packages, setup
from typing import List


def get_requirements(file: str)->List[str]:
    """
    FUNCTION FOR RETURN THE LIST OF REQUIREMENTS
    """
    requirements=[]
    HYPEN_E_DOT="-e ."
    with open(file) as obj:
        requirements=obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ML Project",
    version="0.0.1",
    author="Durga",
    author_email="durganani60@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
