.. -*- coding: utf-8 -*-
...  Copyright 2015 Six Feet Up, Inc.

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.

:title: Pyramid web app
:event: Eleven Fifty
:author: Calvin Hendryx-Parker
:pygments: tango
:css: custom.css

.. |space| unicode:: 0xA0 .. non-breaking space
.. |br| raw:: html
    <br />

----

Introduction to Pyramid - Chapter 2
===============================================

----

Pyramid Workflow

.. note::

    We've done the simplest possible Pyramid app - just a simple Hello World. Now we're going to introduce the standard Pyramid way of setting up a web application.

----


Make a new virtualenv::

    mkvirtualenv pyramid_todo    
    pip install pyramid WebTest

    python --version
    3.4.3

----


Change to your project directory::

    cd C:\Users\[My Username]\Projects\

or::

    cd ~/projects/


----

Pyramid Scaffold::

    pcreate -s alchemy pyramid_todo

    . . . 

    Welcome to Pyramid.  Sorry for the convenience.
    ===============================================================================
.. note::

    We are using the ``pcreate`` command line utility to make us a new Pyramid project with a lot of the configuration already filled in for us. This project will use SQLAlchemy to interact with its data store. The name of the new project is pyramid_todo.

    Pyramid sets up a lot of new files, then prints its rather passive-agressive tagline.

----

Pyramid Scaffold

Let's look around at what Pyramid Scaffold made for us::

    cd pyramid_todo

    tree /f

or::
    
    tree

.. note::

    It set up a whole Pyramid project structure. development.ini is configuration for our development environment, and production.ini is configuration for a production deployment.

    setup.py is an ordinary setuptools file, like you can find in any python project.
----

Going Deeper

Inside the pyramid_todo folder is another pyramid_todo folder. What does it contain?::

    models.py
    tests.py
    views.py
    . . .

.. note::

    Inside the pyramid_todo folder is another pyramid_todo folder. That has files for models, tests and views. We have already seen a simple view, our Hello World page. We have also already written some tests. Models are a new idea. Models define the data needed by our app.

----

Models

.. note::

    TODO talk about Models here

----

Git

Let's get this newly-generated project checked in to git.
    
Change to the new Pyramid app directory::

    cd C:\Users\[My Username]\Projects\pyramid_todo

or::

    cd ~/projects/pyramid_todo

----

Git::

    git init
    git add .
    git commit -m "Inital package from pcreate alchemy scaffold"


----

Install dependencies

The ``pcreate`` utilitu made us a new ``setup.py`` file. We can tell ``pip`` to install this new package and all its dependencies.::

    pip install -e .

.. note::

    Here we are telling pip to install the current folder as an "editable" package. Pip will read the setup.py file, and install the packages that it says it requires.

----






