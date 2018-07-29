[![Build Status](https://travis-ci.org/codylane/ansible-role-pyenv.svg?branch=master)](https://travis-ci.org/codylane/ansible-role-pyenv)

pyenv
=========

Install/Configure and manage [pyenv](https://github.com/pyenv/pyenv)

# Supported Operating Systems

* - EL 6
* - EL 7
* - Ubuntu 14.04
* - Ubuntu 16.04
* - Ubuntu 18.04

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

```
.jenkins/init
. .jenkins-venv/bin/activate
```


# Author Information

* Cody Lane
