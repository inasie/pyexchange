from setuptools import find_packages, setup

setup(
    name='pyexchange',
    version='0.3.16',
    description='Python wrapper of cryptocurrency exchange pubilc APIs',
    url='https://github.com/inasie/pyexchange',
    author='inasie',
    author_email='inasie@naver.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    zip_safe=False
)
