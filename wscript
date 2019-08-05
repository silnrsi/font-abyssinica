#!/usr/bin/python3
# this is a smith configuration file

import glob

APPNAME = "AbyssinicaSIL"
FAMILY = APPNAME
DESC_SHORT = "Unicode font for the Ethiopic script"

getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
BUILDLABEL = "alpha"

fontfamily=APPNAME
designspace('source/' + FAMILY + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            ap = 'source/${DS:FILENAME_BASE}_ap.xml',
            graphite=gdl('./source/Abyssinica_glyphs.gdl',
                    master = 'source/graphite/main.gdl', 
                    params='-D -w3541 -w2504 -w4510',
                    #depends = glob.glob('*.gdh')
                    depends=['source/graphite/main.gdl', 'source/graphite/features.gdh', 'source/graphite/stddef.gdh']
                ),
            opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/master.feax',     # 'source/opentype/${DS:FILENAME_BASE}.fea',
                    mapfile = 'source/${DS:FILENAME_BASE}.map'
                    #params = '-m ' + 'source/${DS:FILENAME_BASE}.map'
                ),
            pdf = fret(params="-r -oi")
)
