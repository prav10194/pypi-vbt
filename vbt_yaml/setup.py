from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Create yaml file for your vbt components'
LONG_DESCRIPTION = 'Create yaml file for your vbt components'

# Setting up
setup(
        name="vbt_yaml", 
        version=VERSION,
        author="<YOUR_NAME>",
        author_email="<PYPI_EMAIL_ID",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=['openpyxl','PyYAML'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
