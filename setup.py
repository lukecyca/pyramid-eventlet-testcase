from setuptools import setup, find_packages

setup(
    name='pyramid-eventlet-testcase',
    version="0.1.0",
    author='Luke Cyca',
    author_email='me@lukecyca.com',

    # File inclusion
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    # Dependencies
    install_requires=[
        'pyramid==1.5a1',
        'eventlet==0.14.0',
        'gunicorn==18.0',
    ],
)
