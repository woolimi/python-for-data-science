from setuptools import setup, find_packages

# build: python setup.py build
# create dist (source dist and built dist)
# python setup.py sdist bdist_wheel
# install
# pip install ./dist/ft_package-0.0.1.tar.gz
# pip install ./dist/ft_package-0.0.1-py3-none-any.whl

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='eagle',
    author_email='eagle@42.fr',
    url='https://github.com/eagle/ft_package',
    license='MIT',
    packages=find_packages(),
)
