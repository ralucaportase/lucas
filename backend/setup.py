from setuptools import setup
from setuptools.command.develop import develop

import distutils.cmd
import os
import subprocess

from importlib import import_module
from subprocess import check_call
from typing import List

localdeps = import_module('localdeps', './localdeps.py')


def pip_install_requirements(requirement_file):
    class Command(develop):
        """This develop command grabs the requirement files for each env
        and installs them using pip.
        """

        user_options = develop.user_options + [('cache=', None, 'Path to cache for. Optional.')]

        def initialize_options(self):
            develop.initialize_options(self)
            self.cache = None

        def run(self):
            base_path = os.path.dirname(os.path.realpath(__file__))
            os.environ['PIP_CONFIG_FILE'] = os.path.join(base_path, 'pip.conf')

            packages = localdeps.read_requirements(requirement_file)
            cache = ['--cache-dir', self.cache] if self.cache else []
            check_call(['pip3', 'install', *packages, *cache])

    return Command


def create_command(text: str, commands: List[List[str]]):
    class CustomCommand(distutils.cmd.Command):
        user_options: List[str] = []
        description = text

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            for cmd in commands:
                subprocess.check_call(cmd)

    return CustomCommand


setup(
    name='lucas',
    version='1.0.0',
    author='Cristi Ingineru, Mihai Toader, Raluca Portase, Teodor Voicencu',
    author_email='some@mail.soon',
    description='The mono-repo filled with spider cuteness.',
    license='Proprietary',
    packages=[],
    cmdclass=dict(
        local=pip_install_requirements('./requirements/development.txt'),
        develop=pip_install_requirements('./requirements/production.txt'),
        format=create_command('Auto-formats code', [['black', '-S', '--config', './pyproject.toml', '.']]),
        verify_format=create_command(
            'Verifies that code is properly formatted',
            [['black', '-S', '--check', '--config', './pyproject.toml', '.']],
        ),
    ),
)
