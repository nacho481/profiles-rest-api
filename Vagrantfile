# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box_download_insecure=true
 config.vm.box = "ubuntu/bionic64" # Base image

 # Configure it to a certain image to prevent any updates to the OS won't
 # effect othe code we have here for this project
# config.vm.box_version = "~> 20200304.0.0"

# Maps a port from our local machine to the machine on our server
# when we run our app, we'' runn it on a network port, accesible from host
# machine or whatever machine, guest machine is the development server

 config.vm.network "forwarded_port", guest: 8000, host: 8000


# This is how we can run scripts when we first create our server
# we disable the update which conflicts with "sudo apt-get update"
# we'll be using python3-venv is a virtual python and it's in a zip
# Create a .bash alias file which ensures Python 3 will be used
#  instead of Python 2.7 so you don't have to type "Python 3" everytime
#  you want to run a command
 config.vm.provision "shell", inline: <<-SHELL
   systemctl disable apt-daily.service
   systemctl disable apt-daily.timer

   sudo apt-get update
   sudo apt-get install -y python3-venv zip
   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end
