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
            ap = 'source/${DS:FILENAME_BASE}_ap.xml',
            opentype = fea('source/${DS:FILENAME_BASE}.fea',
#                    master = 'source/opentype/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/master.feax',
                    ),
            pdf = fret(params="-r -oi")
)
