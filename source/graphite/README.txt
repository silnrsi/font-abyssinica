README
Abyssinica SIL 1.500
========================

This file describes the Graphite source files included with the Abyssinica SIL
font family. This information should be distributed along with the Abyssinica
SIL fonts and any derivative works.

As a reminder: these source files are Copyright (c) 2000-2013, SIL International
(http://scripts.sil.org/) with Reserved Font Names "Abyssinica" and "SIL".
This Font Software is licensed under the SIL Open Font License, Version 1.1.
           
main.gdl     - includes bulk of Graphite rules and extra definitions to support
               them
glyph.gdh    - definition of glyphs and glyph classes; auto-generated from the
               font
features.gdh - feature and language-feature definitions
stddef.gdh   - standard GDL abbreviations

In order to modify the Graphite tables in this font:
* Strip out the existing tables
  Using the Font-TTF-Scripts package ( http://scripts.sil.org/FontUtils ), you
  could use something like:
    ttftable -delete graphite old-font-with-Graphite-tables.ttf  new-font-without-Graphite-tables.ttf 
* Run:
    grcompiler -d -v2 -n2048 -w3521 -w510 font.gdl ttf-file-with-Graphite-tables-stripped.ttf output-ttf.ttf
   