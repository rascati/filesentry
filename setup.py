from setuptools import setup, find_packages

setup(
    name='filesentry',
    version='0.1.0',
    description='Tool to compare two directories and their contents',
    url='https://pypi.python.org/pypi/FileSentry',
    author='Michael Rascati',
    packages=find_packages(),
    install_requires=['filecmp','dircmp','os','sys','colorama'],
    entry_points={
        'console_scripts': [
            'filesentry = filesentry:print_diff_files'
        ]
    }
    zip_safe=False
)
