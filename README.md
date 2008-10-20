dzenlog_text
------------

This is a simple application for textual blog, based on the
[django-dzenlog][] application.

Installation
============

* Install [django-dzenlog][].
* Place dzenlog_text somewhere in your python path.
* Add dzenlog_text to yours INSTALLED_APPS.
* Run `./manager.py syncdb`
* Add this line to the URLConf:  
  `(r'^text/', include('dzenlog_text.urls'))`
* Enjoy you text posts in your blog.

[django-dzenlog]: http://github.com/svetlyak40wt/django-dzenlog
