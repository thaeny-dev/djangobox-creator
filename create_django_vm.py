#!/bin/python
import argparse

import os
import subprocess

from RUtils import make_sure_path_exists

#
#   create_django_vm.py
#
#   Automates creating a directory to do development on a Vagrant virtual machine using Django.
#
#   Created 02/04/2014
#   by Ron Davis, Reactuate Software
#   http://www.reactuatesoftware.com
#

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


def install_cookbooks(in_target_directory):
    """ Creates cookbooks directory in the target directory

    Copies the cookbook folder so we get our custom django cookbook. Then uses  git to get many of the cookbooks

    :type in_target_directory: str
    :param in_target_directory: absolute path to directory we are setting up Vagrant in.
    """
    # copy our cookbook directory
    cp_command = "cp -R cookbooks '{}/'".format(in_target_directory)
    os.system(cp_command)

    # create the cook books directory in target folder if it isn't there already
    new_cookbooks_dir_path = "{}/cookbooks/".format(in_target_directory)
    make_sure_path_exists(new_cookbooks_dir_path)

    # use git to get all the cookbooks
    os.system(git_clone_command("apache2", new_cookbooks_dir_path))
    os.system(git_clone_command("apt", new_cookbooks_dir_path))
    os.system(git_clone_command("build-essential", new_cookbooks_dir_path))
    os.system(git_clone_command("git", new_cookbooks_dir_path))
    #     os.system( git_clone_command("vim", new_cookbooks_dir_path )) # commented out because I don't use vim
    os.system(git_clone_command("openssl", new_cookbooks_dir_path))
    os.system(git_clone_command("postgresql", new_cookbooks_dir_path))
    os.system(git_clone_command("yum", new_cookbooks_dir_path))
    os.system(git_clone_command("python", new_cookbooks_dir_path))


def install_vagrant(in_target_directory):
    """
    Set up the folder for vagrant

    :param in_target_directory: The directory we are setting up Vagrant in.
    """
    # Copy the Vagrant file
    cp_command = "cp Vagrantfile '{}/Vagrantfile'".format(in_target_directory)
    os.system(cp_command)

    # Create the shared directory
    shared_dir_path = make_sure_path_exists("{}/django_shared/".format(in_target_directory))


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

    install_cookbooks(target_dir)
    install_vagrant(target_dir)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()