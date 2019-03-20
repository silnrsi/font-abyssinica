#!/usr/bin/python3
# this is a smith configuration file

APPNAME = "AbyssinicaSIL"
FAMILY = APPNAME
DESC_SHORT = "Unicode font for the Ethiopic script"

getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
BUILDLABEL = "alpha"

fontfamily=APPNAME
designspace('source/' + FAMILY + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi")
)

