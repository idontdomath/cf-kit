from setuptools import setup

setup(
    name='cf-kit',
    version='0.0.1',
    py_modules=['cf-kit'],
    install_requires=[
        'Click','Cloudflare'
    ],
    entry_points='''
        [console_scripts]
        cf-kit=cf_kit:cfkit_cli
    ''',
)