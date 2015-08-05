
Compilation
===========

Configure project by

    ./waf configure

Compile library and test-program like so:

    ./waf build_debug

or

    ./waf build_release

Built artifacts ends up in build-directory.

Run a simple testprogram with:

    build/multineat_main

Including in other projects
===========================

Compile library as described under Compilation. Link to the built
libmultineat.a and include headers under include-dir.
