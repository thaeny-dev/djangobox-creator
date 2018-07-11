#!/bin/python
import argparse

import os
import subprocess
import errno


#
#   create_django_vm.py
#
#   Automates creating a directory to do development on a Vagrant virtual machine using Django.
#
#   Created 02/04/2014
#   by Ron Davis, Reactuate Software
#   http://www.reactuatesoftware.com
#

def make_sure_path_exists(path):
    """ Tries to make a directory. If it exists we just return. 
    
    :param path: path were you want to make sure there is a directory
    :return none
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def git_clone_command(in_cookbook, in_target_directory):
    """ Builds the actual git command to get the named cookbook.

    This assumes you are getting these cookbooks from opscode-cookbooks

    :type in_cookbook: str
    :param in_cookbook: name of the cookbook to be installed
    :param in_target_directory: directory where cookbook should be installed.
    """
    base_command = "git clone git://github.com/opscode-cookbooks/"
    git_base = "{}{}.git".format(base_command, in_cookbook)
    target_path = "{} '{}{}'".format(git_base, in_target_directory, in_cookbook)
    print "----------------------------------------------"
    print "Installing '{}' cookbook".format(in_cookbook)
    print "----------------------------------------------"
    print target_path
    return target_path


def install_vagrant(in_target_directory):
    """
    Set up the folder for vagrant

    :param in_target_directory: The directory we are setting up Vagrant in.
    """
    print("---------------------------------------------")
    print("  Installing vagrant related files")
    print("---------------------------------------------")
    this_file_path = os.path.realpath(__file__)
    this_file_dir = os.path.dirname(this_file_path)
    
    print("Copying Vagrantfile")
    copy_vagrantfile_command = "cp {}/Vagrantfile '{}/Vagrantfile'".format(this_file_dir, in_target_directory)
    os.system(copy_vagrantfile_command)

    # Create the shared directory
    make_sure_path_exists("{}/django_shared/".format(in_target_directory))
    
    print("Copying requirements file")
    cp_requirements_command = "cp {}/requirements.txt '{}/django_shared/requirements.txt'".format(this_file_dir, in_target_directory)
    os.system(cp_requirements_command)
    
    print("Copying copying bookstrap script")
    cp_bootstrap_shell_command = "cp {}/vagrant_install_django_dev.sh '{}/vagrant_install_django_dev.sh'".format(this_file_dir, in_target_directory)
    os.system(cp_bootstrap_shell_command)


def main():
    """
    Parse the arguments and start the work.

    :argument target_directory: path to the directory we are going to create a new Django Vagrant in.

    """
    global g_args

    # argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("target_directory", help="Where you want the VM to be created.", action="store")
    g_args = parser.parse_args()
    target_dir = os.path.abspath(g_args.target_directory)

    if not os.path.exists(target_dir):
        print "Directory '{}' doesn't exist".format(target_dir)
        exit()

    install_vagrant(target_dir)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()