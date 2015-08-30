# hadoop-utils

Various things I've written that I use from time-to-time while dealing with Hadoop.

Contains the following:

###xml_diff

Program that will take two xml properties files and diff them, printing out the diffs without all the XML
stuff.  Differences in both property value and finality are noted.  Also properties which only occur in
one file or the other are noted.

Differences in property values are colorized, and printed in a way where the values line up with each other
so it's hopefully easier to see what is different.

To use it just run:

./xml_diff.py <filea> <fileb>

from within the clone directory.
