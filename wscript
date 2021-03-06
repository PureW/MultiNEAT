#! /usr/bin/env python
# encoding: utf-8
from waflib.Build import BuildContext, CleanContext, \
        InstallContext, UninstallContext

# the following two variables are used by the target "waf dist"
VERSION = '0.0.1'
LIBNAME = 'multineat'
APPNAME = 'multineat_main'

SOURCES_LIB = [
           'src/Genome.cpp',
           'src/Innovation.cpp',
           'src/NeuralNetwork.cpp',
           'src/Parameters.cpp',
           'src/PhenotypeBehavior.cpp',
           'src/Population.cpp',
           'src/PythonBindings.cpp',
           'src/Random.cpp',
           'src/Species.cpp',
           'src/Substrate.cpp',
           'src/Utils.cpp',
           ]
INCLUDES = ['.', 'include']
LIBS = ['m',
        'boost_system']

CPPFLAGS = ['-std=c++11', '-Wall', '-pedantic']
DEFINES=['USE_BOOST_RANDOM']

# these variables are mandatory ('/' are converted automatically)
top = '.'
out = 'build'


def options(opt):
    opt.load('compiler_cxx')

def configure(conf):

    conf.setenv('debug')
    conf.load('compiler_cxx')
    conf.env.CPPFLAGS = ['-g']
    conf.env.LINKFLAGS = ['-g']
    # conf.check(features='c cxx cxxprogram', lib=LIBS, cppflags=CPPFLAGS)

    conf.setenv('release')
    conf.load('compiler_cxx')
    conf.env.CPPFLAGS = [
        '-O2',
        '-march=native',
        ]


def build(bld):
    if not bld.variant:
        bld.fatal('call "waf build_debug" or "waf build_release", '
                  'and try "waf --help"')

    bld.env.DEFINES = ['USE_BOOST_RANDOM=1']

    bld.stlib(source=SOURCES_LIB,
              target=LIBNAME,
              includes=INCLUDES,
              cppflags=CPPFLAGS,
              lib=LIBS,
              # linkflags=['-pg'],
              )
    bld.program(source='src/Main.cpp',
                target=APPNAME,
                includes=INCLUDES,
                cppflags=CPPFLAGS,
                lib=LIBS,
                use=LIBNAME,
                defines=['USE_BOOST_RANDOM'],
                # linkflags=['-pg'],
                )


for x in ['debug', 'release']:
    for y in (BuildContext, CleanContext, InstallContext, UninstallContext):
        name = y.__name__.replace('Context', '').lower()

        class tmp(y):
            cmd = name + '_' + x
            variant = x
