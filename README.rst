Engine for http://bluxte.net/
=============================

This is the Pelican_ configuration, plugins and theme for http://bluxte.net.

Actual content is held in a private repository, where I can keep my dirty little secrets
(aka draft posts and other non publicly-linked files) away from curious visitors!

The Python environment can be setup by running ``pip install -r requirements.txt`` in a virtualenv.
I highly recommend virtualenvwrapper_ to manage your virtualenvs.

.. _Pelican: http://blog.getpelican.com/
.. _virtualenvwrapper: https://bitbucket.org/dhellmann/virtualenvwrapper

The structure of my setup is a follows:

.. code::

    engine/  <-- this repository
    website/ <-- private repository
      content/
      Makefile
      publishconf.py
