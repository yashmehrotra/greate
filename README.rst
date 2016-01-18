Greate
======

Greate helps you in creating github repos on the go from your command line.
All you have to do is write :code:`greate` and it will create a repository with the name of your current directory.

You can also customize your repository by using additional arguments

Installation
------------
.. code-block:: sh

    $ pip install git+https://github.com/yashmehrotra/greate.git


Usage
-----

.. code-block:: ssh

    usage: greate [-h] [--ssh] [-d DESCRIPTION] [-n NAME] [-r] [-p]

    optional arguments:
      -h, --help            show this help message and exit
      --ssh                 Adds the ssh url for git remote. Default: https
      -d DESCRIPTION, --description DESCRIPTION
                            Description for github repo
      -n NAME, --name NAME  Name for the github repo. Default: Current directory name
      -r, --readme          Create README.md for github repo
      -p, --private         Private github repo



Examples
--------
.. code-block:: sh

    $ greate
    Username: foobar
    Password: 
    Repository created successfully

    # Use ssh as remote url
    $ greate --ssh
    Username: foobar
    Password: 
    Repository created successfully

    # Add description
    $ greate -d "My first project"
    Username: foobar
    Password: 
    Repository created successfully


TODO
----

1. Clean Code