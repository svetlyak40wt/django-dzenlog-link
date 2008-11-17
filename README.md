dzenlog_text
------------

This is a simple application to post links to the blog, based on the
[django-dzenlog][] application.

Installation
============

* Install [django-dzenlog][].
* Place `dzenlog_text` somewhere in your python path.
* Add `dzenlog_link` to yours `INSTALLED_APPS`.
* Run `./manager.py syncdb`
* Add this line to the URLConf:

        (r'^text/', include('dzenlog_link.urls'))

* Enjoy link posts in your blog.

[django-dzenlog]: http://github.com/svetlyak40wt/django-dzenlog
