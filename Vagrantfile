# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "lucid64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/lucid64.box"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8000, host: 8000

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.

  # made a folder for doing django and for putting some scripts we'll use later.
  config.vm.synced_folder "django_shared", "/home/vagrant/django_shared"
  
  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
    config.vm.provision :chef_solo do |chef|
        #chef.log_level = :debug
        chef.json = {
            postgresql: {
                password: {
                    postgres: 'password'
                    },
                    pg_hba: [
                      {type: 'local', db: 'all', user: 'all', addr: nil, method: 'trust'},
                      {type: 'host', db: 'all', user: 'all', addr: '127.0.0.1/32', method: 'trust'},
                      {type: 'host', db: 'all', user: 'all', addr: '::1/128', method: 'trust'}
                    ]
            },
            python:{install_method:'source', version:'2.7.3', checksum: 'c57477edd6d18bd9eeca2f21add73919'}
        }        
        chef.cookbooks_path = "cookbooks"
        chef.add_recipe "apt"
        chef.add_recipe "apache2::mod_wsgi"
        chef.add_recipe "build-essential"
        chef.add_recipe "git"
        chef.add_recipe "postgresql"
        chef.add_recipe "postgresql::server"
        chef.add_recipe "python"
        chef.add_recipe "django"
    end
end
