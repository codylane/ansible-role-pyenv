[![Build Status](https://travis-ci.org/codylane/ansible-role-pyenv.svg?branch=master)](https://travis-ci.org/codylane/ansible-role-pyenv)

pyenv
=========

Install/Configure and manage [pyenv](https://github.com/pyenv/pyenv)

# Supported Operating Systems

* - EL 6
* - EL 7
* - Debian jessie
* - Debian stretch
* - Debian buster
* - Ubuntu trusty
* - Ubuntu xenial
* - Ubuntu bionic

# Role Variables

# Defaults

* See the [defaults](defaults/main.yml)

#### `pyenv_git_version`

* The git version of pyenv to install. Default: `master`


#### `pyenv_git_update`

* Whether or not to upgrade pyenv when ansible runs. Default: `true`

#### `pyenv_root`

* The full path to where pyenv will be installed. Default: `/opt/pyenv`


#### `pyenv_profiled_script`

* The full path to the profile script that activates pyenv. Default: `/etc/profile.d/pyenv.sh`


#### `pyenv_user`

* The user for PYENV_ROOT. Default: `root`


#### `pyenv_group`

* The group for PYENV_ROOT. Default: `root`

#### `pyenv_install_these_pythons`

* A list of pythons to install. Default:

```
- 2.6.9
- 2.7.15
- 3.4.8
- 3.5.5
- 3.6.6
- 3.7.0
```

# Dependencies

* None

# Example with custom params

```
---

- name: An example playbook
  hosts: all

  roles:
    - role: codylane.pyenv
      pyenv_root: /var/lib/jenkins/.pyenv
      pyenv_user: jenkins
      pyenv_group: jenkins
      pyenv_install_these_pythons:
        - 2.6.9
        - 2.7.15
        - 3.7.0
```


# License

MIT

# Ansible Testing Requirements

* We use the awesome [invoke](http://www.pyinvoke.org/) python library of wrapping how we test.
* Molecule is being as a test harness but we use `invoke` to provide some additional bootstraping.


* We first setup our test environment, install pyenv, some pythons, our test requirements... etc.
```
.jenkins/init-pyenv
```

#### When testing in travis

##### travis usage `.jenkins/run-pyenv 'invoke travis -h'`

```
Usage: inv[oke] [--core-opts] travis [--options] [other tasks here ...]

Docstring:
  Run our tests but help travis along

Options:
  -d, --[no-]destroy
  -p, --[no-]pty
  -s, --scenario
```

* Here is an example of testing just the `default` molecule role

```
.jenkins/run-pyenv 'invoke travis'
```

* See [.travis.yml](.travis.yml) for more info


# Author Information

* Cody Lane
