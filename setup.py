from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in buzola_custom/__init__.py
from buzola_custom import __version__ as version

setup(
	name="buzola_custom",
	version=version,
	description="Adecuaciones realizadas a erpnext para el funcionamiento deseado de erpnext",
	author="buzola",
	author_email="admin@appcity.mx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
