About this product
==================

This product makes it possible to export collections as CSV.
The base code is stolen from Pilot Systems' Smart CSV Exporter.

Tested on:
* Plone 3.2.3 (Unified installer)
* Plone 4.0.1 (Unified installer)

Why does it exist?
==================

Smart CSV Exporter didn't work for me, it returned an error with custom collection indexes and metadata.
It turned out to be the part that was added in order to play nice with lists and objects.
Since there was no eggefied version of the product, I decided to make a new one:)

Differences from Smart CSV Exporter
===================================

* Buildout can be used to grab the product
* Play nice with lists and objects part removed
* CSV settings have seperate properties on the tool
* Authenticated with view permission can export an collection

How to use ?
============

After installing the package (see docs/INSTALL.txt), restart Zope.

Go to Plone configuration menu "Add/Remove product", select the product and install it.

Now each collection has a new tab called "CSV Export", click it to generate a CSV-file.

Only the fields listed in the collections 'Table Columns' are exported, even if the table view isn't used.

Have fun !

Options
=======

When the product is installed, a tool is created in the root of your site, named "colport_tool".

Here four options regarding the CSV generation can be changed:
* csv_delimiter: A one-character string used to separate fields. The default is ';'.
* csv_quotechar: A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. The default is '"'.
* csv_skipinitialspace: When True, whitespace immediately following the delimiter is ignored. The default is False.
* csv_quoting: Defines on which fields the quotechar is used, accepts the following values:
    - QUOTE_ALL: Instructs writer objects to quote all fields.
    - QUOTE_MINIMAL: Instructs writer objects to only quote those fields which contain special 
                     characters such as delimiter, quotechar or any of the characters in lineterminator.
    - QUOTE_NONNUMERIC: Instructs writer objects to quote all non-numeric fields.
                        Instructs the reader to convert all non-quoted fields to type float.
    - QUOTE_NONE: Instructs writer objects to never quote fields. When the current delimiter 
                  occurs in output data it is preceded by the current escapechar character. 
                  If escapechar is not set, the writer will raise Error if any characters that 
                  require escaping are encountered.
                  Instructs reader to perform no special processing of quote characters

Todo
====

* Include tests
* It's probably usefull to let the user know an error occured instead of just logging it


    
  

