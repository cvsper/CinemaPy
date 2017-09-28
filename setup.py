from setuptools import setup, find_packages

setup(
	name='moviePy',
	version='0.1.0',
	description='Watch movies',
	license='MIT',
	install_requires=['requests','BeautifulSoup' ],
	packages=find_packages(),
	scripts='moviepy.py'


	)