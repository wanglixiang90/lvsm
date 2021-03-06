Changes
========

0.5.1 (2014-11-18)
------------------

* Finalizing release
* Added some features

0.5.1 (2014-02-23)
------------------

* Lots of bug fixes
* Added ability to handle templating of configs

0.5.0 (2014-01-29)
------------------

* Complete redo of the syntax 
* Added support for keepalived
* Added support for git (limited)

0.4.1 (2013-06-21)
------------------

* Added use of logging module
* Fixed bug where non-standard port number would crash the app

0.4.0 (2013-04-11)
------------------

* Added ldirectord config parsing
* Fixed logic errors in "config edit"
* Fixed bug with genericdirector
* Updated test cases

0.3.5 (2013-04-04)
------------------

* Fixed regression bug with director.show
* Fixed logic error in director.enable
* PEP8-ified

0.3.4 (2013-02-17)
------------------

* Fixed minor issue with enable
* Fixed minor issue with firewall.show_virtual
* added config item to define what scm to use
* director.show now displays disabled hosts 

0.3.3 (2013-02-05)
------------------

* Fixed pagination
* Added colour support to ipvsadm and iptables output
* enable/disable commands now ensure the RIP is enabled/disabled
* enable/disable now work across a cluster (if defined)
* General bug fixes

0.3.2 (2013-01-13)
------------------

* Fixed bug when quitting and no files are modified
* Added pagination support for long output
* Added new "status show nat" command
* refactored Director classes to use a factory pattern
* Added stub Keepalived class


0.3.1 (2013-01-09)
------------------

* Added color term support
* Added verification of modified configs
* refactored CommandPrompt and Director classes
* Fixed typos 


0.3.0 (2012-11-06)
------------------

* Added ability to restart firewall and director
* Added ``--version`` flag 
* Fixed bug with unhelpful ipvsadm error message
* Fixed bug in firewall module's ``show()``  


0.2.1 (2012-10-22)
------------------

* Bug fixes in Director class

0.2.0 (2012-10-21)
------------------

* Bug fixes
* Disabling real servers now prompts user for a comment
* ``show virtual`` now displays firewall info for VIP

0.1.1 (2012-10-17)
------------------

* Bug fixes

0.1.0 (2012-10-16)
------------------

* Initial relase 
