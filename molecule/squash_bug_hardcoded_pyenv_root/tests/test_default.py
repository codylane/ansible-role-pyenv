# coding: utf-8
# flake8: noqa

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def assert_pip_package_version_is_installed(packages, expected_pkg_name, expected_version):
    """Expect host.pip_package(expected_pkg_name).version == expected_version

    """

    assert expected_pkg_name in packages, 'The PIP package `{}` is not installed'.format(expected_pkg_name)
    pkg = packages[expected_pkg_name]

    err_msg = 'Expected package `{}` version == `{}`, got `{}`'.format(expected_pkg_name, expected_version, pkg['version'])

    if expected_version:
        assert pkg['version'] == expected_version, err_msg


def test_pyenv_root_is_set_to_slash_root_slash_dot_pyenv(host):
    pyenv_root = host.file('/root/.pyenv')

    assert pyenv_root.exists
    assert pyenv_root.is_directory
    assert pyenv_root.user == 'jenkins'
    assert pyenv_root.group == 'jenkins'


def test_pyenv_root_versions_2715_is_a_directory(host):
    pyenv_root = host.file('/root/.pyenv/versions/2.7.15')

    assert pyenv_root.exists
    assert pyenv_root.is_directory
    assert pyenv_root.user == 'jenkins'
    assert pyenv_root.group == 'jenkins'


def test_python2715_pip_package_is_installed(host):
    packages = host.pip_package.get_packages(pip_path='/root/.pyenv/versions/2.7.15/bin/pip')
    expected_packages = (
        dict(expected_pkg_name='pip',               expected_version='10.0.1'),
        dict(expected_pkg_name='invoke',            expected_version=None),
        dict(expected_pkg_name='virtualenv',        expected_version=None),
        dict(expected_pkg_name='virtualenvwrapper', expected_version=None),
    )

    for expected_pkg in expected_packages:
        assert_pip_package_version_is_installed(packages, expected_pkg['expected_pkg_name'], expected_pkg['expected_version'])
