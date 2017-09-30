from distutils.core import setup

setup(
    name='multi-logger',
    version='0.1',
    packages=['multilogger'],
    url='https://github.com/ahmedrshdy/multi-logger',
    license='proprietary',
    author='Ahmed Roshdy',
    author_email='a.elshalaby@e-tawasol.com',
    description='Multi channel configurable logger',
    install_requires=[
        'watchtower',
        'boto3'
    ]
)

