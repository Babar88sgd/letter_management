from setuptools import find_packages, setup

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")
	install_requires = [r for r in install_requires if r]

# get version from __version__ variable in letter_management/__init__.py
from letter_management import __version__ as version

setup(
	name="letter_management",
	version=version,
	description="Directly-created, role-restricted Official Letters with company-specific Letter Heads.",
	author="Babar Mehmood",
	author_email="you@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
