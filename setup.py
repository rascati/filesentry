from setuptools import setup, find_packages

setup(
    name='filesentry',
    packages=['filesentry'],
    version='0.1.0',
    description='Tool to compare two directories and their contents',
    author='Michael Rascati',
    author_email='rascatimichael@gmail.com',
    url='https://github.com/rascati/filesentry',
    download_url = 'https://github.com/rascati/filesentry/archive/0.1.0.tar.gz',


    # packages=find_packages(),
    # install_requires=['filecmp','dircmp','os','sys','colorama'],
    # # entry_points={
    # #     'console_scripts': [
    # #         'filesentry = filesentry:print_diff_files'
    # #     ]
    # # }
    # zip_safe=False
)
