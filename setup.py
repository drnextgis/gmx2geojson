from setuptools import setup

setup(
    name='gmx2geojson',
    version='0.1',
    py_modules=['gmx2geojson'],
    include_package_data=True,
    install_requires=[
        'click',
        'geojson'
    ],
    entry_points='''
        [console_scripts]
        gmx2geojson=gmx2geojson:main
    ''',
)

