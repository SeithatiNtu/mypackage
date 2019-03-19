from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Analyse Hackathon Project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/SeithatiNtu/mypackage.git',
    author='Phomolo',
    author_email='ntumelang@gmail.com'
)
