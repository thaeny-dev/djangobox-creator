#!/bin/python
import argparse

import os
import subprocess

from RUtils import make_sure_path_exists

def git_clone_command(in_cookbook, in_target_directory):
    ''' builds the actual git command to run '''
    base_command = "git clone git://github.com/opscode-cookbooks/"
    git_base = "{}{}.git".format( base_command, in_cookbook )
    target_path = "{} '{}{}'".format( git_base, in_target_directory, in_cookbook )
    print "----------------------------------------------\nInstalling '{}' cookbook\n----------------------------------------------".format(in_cookbook)
    print target_path
    return target_path

def install_cookbooks(in_target_directory):
    ''' Git clones cookbooks into target directory '''
    cp_command = "cp -R cookbooks '{}/'".format( in_target_directory ) 
    print cp_command
    os.system(cp_command)
    
    # create the cook books directory in target folder
    new_cookbooks_dir_path = "{}/cookbooks/".format( in_target_directory )
    make_sure_path_exists(new_cookbooks_dir_path)

    # use git to get all the cookbooks
    os.system( git_clone_command("apache2", new_cookbooks_dir_path ))
    os.system( git_clone_command("apt", new_cookbooks_dir_path ))
    os.system( git_clone_command("build-essential", new_cookbooks_dir_path ))
    os.system( git_clone_command("git", new_cookbooks_dir_path ))
#     os.system( git_clone_command("vim", new_cookbooks_dir_path ))
    os.system( git_clone_command("openssl", new_cookbooks_dir_path ))
    os.system( git_clone_command("postgresql", new_cookbooks_dir_path ))
    os.system( git_clone_command("yum", new_cookbooks_dir_path ))
    os.system( git_clone_command("python", new_cookbooks_dir_path ))

def install_vagrant(in_target_directory):
    # copy the vagrant file
    cp_command = "cp Vagrantfile '{}/Vagrantfile'".format( in_target_directory )
    print cp_command
    os.system( cp_command )
    
    # create the shared directory
    shared_dir_path = make_sure_path_exists( "{}/django_shared/".format( in_target_directory ) )
    
    
def main():
    global g_args

    # argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("target_directory", help="Where you want the VM to be created.", action="store")
    g_args = parser.parse_args()
    target_dir = os.path.abspath(g_args.target_directory)

    if not os.path.exists(target_dir):
        print "Directory '{}' doesn't exist".format( target_dir )
        exit()
    
    install_cookbooks(target_dir)
    install_vagrant(target_dir)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()