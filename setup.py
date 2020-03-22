from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='fakerabbit',
    version='0.2.2',
    description='A simple lib to make fake objects using SQLAlchemy',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Josenildo Junior',
    author_email='josenildoaf@gmail.com',
    keywords=['Factory', 'Fake', 'SQLAlchemy', 'Tests'],
    url='https://github.com/fariias/fake_rabbit.git',
    download_url='https://github.com/fariias/fake_rabbit.git'
)

install_requires = [
    'SQLAlchemy'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
