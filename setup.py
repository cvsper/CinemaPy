from setuptools import setup, find_packages

setup(
	name='cinemaPy',
	version='0.1.0',
	description='Watch streaming movies',
	license='MIT',
	install_requires=['requests','BeautifulSoup', 'lxml', 'html.parser' ],
	packages=find_packages(),
	scripts='moviepy.py'


	)