import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='bigcommerce_3',
      version='0.1',
      packages=find_packages(),
      install_requires = ['requests>=2.1.0', 'pyjwt>=1.4.0'],
      description='Connect Python applications with the Bigcommerce API v3 Cart and Script',
      url='https://github.com/IrinaMityayeva/bigcommerce-api-python',
      author='Miaskad',
      author_email='miaskad@gmail.com',
      license='MIT',
      zip_safe=False)

