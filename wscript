#!/usr/bin/python3
# this is a smith configuration file for Abyssinica font project

# override the default folders
DOCDIR = ['documentation', 'web']  # add 'web' to default
generated = 'generated/'

# set package name
APPNAME = 'AbyssinicaSIL'

# set the font family name
FAMILY = APPNAME

#import glob

# set the default output folders
out = "results"  # default is currently buildlinux2
# OUTDIR = "installers"  # until these are defaults in smith itself we need to keep them
ZIPDIR = "releases"
TESTDIR = "tests"

getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')

ftmlTest('tests/ftml-smith.xsl', fonts = ['reference/AbyssinicaSIL-Regular.ttf'], addfontindex = 1, fontmode = 'collect')

designspace('source/' + FAMILY + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            ap = generated + '${DS:FILENAME_BASE}_ap.xml',
            version = VERSION,  # Needed to ensure dev information on version string
            graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
                    master = 'source/graphite/main.gdl', 
                    params = '-D -w3541 -w2504 -w4510',
                    #depends = glob.glob('*.gdh')
                    depends = ['source/graphite/main.gdl', 'source/graphite/features.gdh', 'source/graphite/stddef.gdh']
                ),
            opentype = fea(generated + '${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/master.feax', 
                    mapfile = generated + '${DS:FILENAME_BASE}.map'
                ),
            typetuner = typetuner("source/typetuner/feat_all.xml"),
            script = 'ethi',
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/' + FAMILY + '-WOFF-metadata.xml'),
    )
