import setuptools

setuptools.setup(
    name='true-case-path',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
