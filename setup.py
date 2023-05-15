import io
from os.path import abspath, dirname, join
import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
    name='micropython-googlesheet',
    py_modules=['ggsheet'],
    version='0.0.2',
    description='Update or append the data to Google Sheet, or get the data on Google Sheet. by using HTTP to execute the Google Apps Script API compatible with ESP32 and ESP8266.',
    long_description=DESCRIPTION,
    keywords= ['googlesheet', 'esp32', 'esp8266' ,'micropython'],
    url='https://github.com/PerfecXX/MicroPython-GoogleSheet',
    author='Teeraphat Kullanankanjana',
    author_email='ku.teeraphat@hotmail.com',
    maintainer='Teeraphat Kullanankanjana',
    maintainer_email='ku.teeraphat@hotmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 3 - Alpha', 
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)
