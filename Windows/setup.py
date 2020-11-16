from setuptools import setup

with open('./README.md') as f:
  readme = f.read()

setup(
    name='doorman-win',
    version='0.0.1',
    description='CINS548 - Group 3 - Doorman - Windows',
    long_description=readme,
    author='CINS548 - Group 3',
    url='https://github.com/hzlleo/CINS548_Group03'
)
