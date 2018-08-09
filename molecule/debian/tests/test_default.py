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


@pytest.mark.parametrize(
    'required_package, what_package_install_should_be',
    (
        pytest.param('build-essential', True),
        pytest.param('curl', True),
        pytest.param('git', True),
        pytest.param('libapt-pkg-dev', True),
        pytest.param('libbz2-dev', True),
        pytest.param('libffi-dev', True),
        pytest.param('libncurses5-dev', True),
        pytest.param('libncursesw5-dev', True),
        pytest.param('libreadline-dev', True),
        pytest.param('libsqlite3-dev', True),
        pytest.param('llvm', True),
        pytest.param('make', True),
        pytest.param('tk-dev', True),
        pytest.param('wget', True),
        pytest.param('xz-utils', True),
        pytest.param('zlib1g-dev', True),
    ),
)
def test_required_package_is_installed(host, required_package, what_package_install_should_be):
    package = host.package(required_package)

    assert package.is_installed is what_package_install_should_be



@pytest.mark.parametrize(
    'required_package, what_package_install_should_be',
    (
        pytest.param('libssl-dev', True),
    ),
)
def test_required_package_is_installed_on_1604(host, required_package, what_package_install_should_be):
    if host.system_info.release != '16.04':
        pytest.skip('Skipping tests because host is not 16.04')

    package = host.package(required_package)

    assert package.is_installed is what_package_install_should_be


@pytest.mark.parametrize(
    'required_package, what_package_install_should_be',
    (
        pytest.param('libssl1.0-dev', True),
    ),
)
def test_required_package_is_installed_on_1804(host, required_package, what_package_install_should_be):
    if host.system_info.release != '18.04':
        pytest.skip('Skipping tests because host is not 18.04')

    package = host.package(required_package)

    assert package.is_installed is what_package_install_should_be


def test_pyenv_root_dir_exists(host):
    opt_pyenv = host.file('/opt/pyenv')

    assert opt_pyenv.exists
    assert opt_pyenv.is_directory
    assert opt_pyenv.user == 'root'
    assert opt_pyenv.group == 'root'


def test_etc_profile_dot_d_pyenv_dot_sh_exists(host):
    etc_profiled_pyenv_sh = host.file('/etc/profile.d/pyenv.sh')

    expected_content = '''export PYENV_ROOT="${PYENV_ROOT:-/opt/pyenv}"
export PATH="${PYENV_ROOT}/bin:${PATH}"
eval "$(pyenv init -)"
[ -d "${PYENV_ROOT}/plugins/pyenv-virtualenv" ] && eval "$(pyenv virtualenv-init -)"
'''

    assert etc_profiled_pyenv_sh.exists
    assert etc_profiled_pyenv_sh.is_file
    assert etc_profiled_pyenv_sh.user == 'root'
    assert etc_profiled_pyenv_sh.user == 'root'
    assert etc_profiled_pyenv_sh.mode== 0o0644
    assert etc_profiled_pyenv_sh.content_string.strip() == expected_content.strip()


@pytest.mark.parametrize(
    'version',
    (
        pytest.param('2.6.9'),
        pytest.param('2.7.15'),
        pytest.param('3.6.6'),
    ),
)
def test_opt_python_version_dir_exists(host, version):
    directory = host.file('/opt/python/{version}'.format(version=version))

    assert directory.exists
    assert directory.is_directory
    assert directory.user == 'root'
    assert directory.group == 'root'
    assert directory.mode == 0o0755

    python_version_file = host.file('/opt/python/{version}/.python-version'.format(version=version))

    assert python_version_file.exists
    assert python_version_file.is_file
    assert python_version_file.user == 'root'
    assert python_version_file.group == 'root'
    assert python_version_file.mode== 0o0644


def test_python269_pip_package_is_installed(host):
    packages = host.pip_package.get_packages(pip_path='/opt/pyenv/versions/2.6.9/bin/pip')
    expected_packages = (
        dict(expected_pkg_name='pyOpenSSL',         expected_version='17.5.0'),
        dict(expected_pkg_name='pip',               expected_version='9.0.3'),
        dict(expected_pkg_name='ndg-httpsclient',   expected_version='0.5.0'),
        dict(expected_pkg_name='pyasn1',            expected_version=None),
        dict(expected_pkg_name='invoke',            expected_version=None),
        dict(expected_pkg_name='virtualenv',        expected_version=None),
        dict(expected_pkg_name='virtualenvwrapper', expected_version=None),
    )

    for expected_pkg in expected_packages:
        assert_pip_package_version_is_installed(packages, expected_pkg['expected_pkg_name'], expected_pkg['expected_version'])


def test_python2715_pip_package_is_installed(host):
    packages = host.pip_package.get_packages(pip_path='/opt/pyenv/versions/2.7.15/bin/pip')
    expected_packages = (
        dict(expected_pkg_name='pip',               expected_version='10.0.1'),
        dict(expected_pkg_name='invoke',            expected_version=None),
        dict(expected_pkg_name='virtualenv',        expected_version=None),
        dict(expected_pkg_name='virtualenvwrapper', expected_version=None),
    )

    for expected_pkg in expected_packages:
        assert_pip_package_version_is_installed(packages, expected_pkg['expected_pkg_name'], expected_pkg['expected_version'])


def test_python366_pip_package_is_installed(host):
    packages = host.pip_package.get_packages(pip_path='/opt/pyenv/versions/3.6.6/bin/pip')
    expected_packages = (
        dict(expected_pkg_name='pip',               expected_version='10.0.1'),
        dict(expected_pkg_name='invoke',            expected_version=None),
        dict(expected_pkg_name='virtualenv',        expected_version=None),
        dict(expected_pkg_name='virtualenvwrapper', expected_version=None),
    )

    for expected_pkg in expected_packages:
        assert_pip_package_version_is_installed(packages, expected_pkg['expected_pkg_name'], expected_pkg['expected_version'])


@pytest.mark.parametrize(
    'plugin',
    (
        pytest.param('pyenv-virtualenv'),
    ),
)
def test_activated_plugins_are_installed(host, plugin):
    path = host.file('/opt/pyenv/plugins/' + plugin)

    assert path.exists
    assert path.is_directory
    assert path.user == 'root'
    assert path.group == 'root'
    assert path.mode == 0o0755
