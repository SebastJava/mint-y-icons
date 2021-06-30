![colors-preview](colors-preview.png)

Mint-Yz-icons is forked from Mint-Y-icons
=========================================

These icons are the same as those found in Mint-Y icons. Only the places colors have been changed to match the colors of https://github.com/SebastJava/mint-yz-theme.

Installation
============

1. Go to the [Releases](https://github.com/SebastJava/mint-yz-icons/releases) page. Select the latest.
1. Click on **Assets** to see the files if needed. (under the short presentation)
1. Download the **.deb** (Debian package) file.
1. Open it and click the **[Install Package]** button.
1. Select your new icons in **Menu > Preferences > Themes**

Credits
=======

The application and category icons originate from the Moka icon theme:

* Link: https://github.com/moka-project/moka-icon-theme
* Author: Sam Hewitt <hewittsamuel@gmail.com>
* License: Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0)

The folder icons originate from the Arc icon theme:

* Link: https://github.com/horst3180/arc-icon-theme
* Author: horst3180 (http://horst3180.deviantart.com)
* License: GPLv3

The device icons originate from the Paper icon theme:

* Link: https://github.com/snwh/paper-icon-theme
* Author: Sam Hewitt <hewittsamuel@gmail.com>
* License: Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0)

The mimetype icons originate from the Elementary icon theme:

* Link: https://github.com/elementary/icons
* Author: Members of the Elementary OS team (https://github.com/orgs/elementary/people)
* License: GPLv3 (https://choosealicense.com/licenses/gpl-3.0/)

The action and panel icons originate from the ePapirus theme:

* Link: https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
* Author: Members of the Papirus Development Team (https://github.com/orgs/PapirusDevelopmentTeam/people)
* License: GPLv3 (https://choosealicense.com/licenses/gpl-3.0/)

License
=======

This theme is licensed under Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0).

Any bundled software is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version.

Useful commands
===============

To find circular symbolic links:

	find . -follow -printf ""

To find broken links use `./deadlinks` or:

	find -L usr/ -type l

To find files with spaces in their filenames (that breaks the icon cache generation):

	find . | egrep '. '

Build step-by-step
==================

NOTE: My-complete-step-by-step.txt is the new "Build step-by-step". This one here is probably out-of-date but was not deleted because it contains some more detailed instructions.
 
First, open your Terminal and type:

	git clone https://github.com/SebastJava/mint-yz-icons.git

To build your own icon theme, you will need to install those packages:
 
  * Inkscape, preferably version 1.0 or higher (from PPA?)
  * optipng
  * git

Edit the color hex values in **src/places/generate-color-variations.py.** You can also add or delete color names there. Do not change `GREEN_COLOR = "8bb158"`. This one is used by the `sed` find and replace command.

This also means that the ~/mint-yz-icons/src/places/green.svg must not be changed in any way. This one is the template from which all the other colors are build.

If you added or removed color names, you also need to edit the colors array in **src/render_places.py** and the names array in **make-directories-and-index.sh**

Next, open your Terminal and do these lines, one by one:

	shopt -s extglob # enable the extglob shell option
	cd ~/mint-yz-icons/usr/share/icons # go there
	rm -rf !(Mint-Yz-Classic|Mint-Yz-Classic-Dark) # delete old icons except Mint-Yz-Classic + Mint-Yz-Classic-Dark
	cd ~/mint-yz-icons/src/places # go there
	rm -- !(green.svg|extra.svg|*.py) # remove all except extra, generate-color-variations, and green
	shopt -u extglob # turn off the extglob shell option
	./generate-color-variations.py # run this
	cd .. # move up
	./render_places.py All # run this
	cd .. # move up
	./make-directories-and-index.sh # run this
	sudo rm -rf /usr/share/icons/Mint-Yz-* # quick test
	sudo cp -rf usr/share/icons/Mint-Yz-* /usr/share/icons/ # quick test

Next, edit these files:

  * debian/changelog
  * debian/control
  * debian/copyright

If you added or removed color names, you also need to update this file:

  * debian/postinst (Make sure your text editor replaces each tab with 4 spaces!)

And now you can build the Debian package:

	dpkg-buildpackage # build Debian package

Now, go in Menu > Preferences > Themes and try your new icons!
