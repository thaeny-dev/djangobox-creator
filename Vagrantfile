# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "ubuntu/xenial64"
    _local_vagrant_box = "/opt/vagrant-boxes/xenial-server-cloudimg-amd64-vagrant.box"
  	if File.exists?(_local_vagrant_box)
        config.vm.box_url = "file://" + _local_vagrant_box
    else
        config.vm.box_version = ">= v20180710.0.0 "
  	end

    # set the name of the box to make it a little easier to find in virtual box
    config.vm.provider "virtualbox" do |custom_virtualbox_settings|
      custom_virtualbox_settings.name = "djangobox"
    end

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine. In the example below,
    # accessing "localhost:8080" will access port 80 on the guest machine.
    config.vm.network :forwarded_port, guest: 80, host: 9080
    config.vm.network :forwarded_port, guest: 8000, host: 9000

    # made a folder for doing django and for putting some scripts we'll use later.
    config.vm.synced_folder "django_shared", "/home/vagrant/django_shared"

    # let this shell script do the installation of everything you need to do django dev    
    config.vm.provision :shell, :path => "vagrant_install_django_dev.sh"

end
