# Djangobox-Creator
A small script and set of configurations to create a Vagrant-Box for Django-Development

Fork from: https://bitbucket.org/rondavis007/django-vagrant-creation-scripts.git
(upgraded to python3/Django2, removed all the chef-stuff)

Future: replace shell-script by ansible-plabooks

## Installation
```
python create_django_vm.py /path/to/project/djangobox
```
At the moment only Python2 is supported for the creator-script (python3-support will follow)

As a result a directory with the following content will be created
```
django_shared
    requirements.txt
Vagrantfile
vagrant_install_django_dev.sh
```

Change to the target-directory and execute `vagrant up`

```
cd /path/to/project/djangobox
vagrant up
```

As result you will have a full django-installation with the necessary requirements.

