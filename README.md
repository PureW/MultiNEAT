
About MultiNEAT
===============

What is it?
------------

MultiNEAT is a portable software library for performing neuroevolution, a form of machine learning that trains neural networks with a genetic algorithm. It is based on NEAT, an advanced method for evolving neural networks through complexification. The neural networks in NEAT begin evolution with very simple genomes which grow over successive generations. The individuals in the evolving population are grouped by similarity into species, and each of them can compete only with the individuals in the same species. The combined effect of speciation, starting from the simplest initial structure and the correct matching of the genomes through marking genes with historical markings yields an algorithm which is proven to be very effective in many domains and benchmarks against other methods. NEAT was developed around 2002 by Kenneth Stanley in the University of Texas at Austin.

HyperNEAT
---------

HyperNEAT is an extension to NEAT by David D'Ambrosio, Jason Gauci and Kenneth Stanley, where the phenotypes are derived indirectly from special kind of neural networks known as Compositional Pattern Producing Networks (CPPNs). The genotypes are CPPNs evolved with NEAT, while the phenotypes are neural networks which have geometric structure. NEAT is used to find the underlying geometric relationships of the problem, and the produced neural networks can have millions of neurons and connections.


Novelty Search
--------------


Novelty Search is a method of search by Joel Lehman and Kenneth Stanley that drops the concept of objectives and searches instead for novelty of phenotypic behaviors. The method itself is not constrained to NEAT and can be used with any genetic encoding, but NEAT is advantageous as genotypic complexity often correlates with behavior complexity, so NEAT searches the behavior space more effectively. The method has shown very promising results and is proven effective in tasks with deceptive fitness landscapes where regular objective-based methods are trapped in local optimums.


MultiNEAT
---------

MultiNEAT was originally named NSNEAT. It was a generic NEAT implementation by Peter Chervenski and Shane Ryan, created while working for NEAT Sciences Ltd in 2007-2008. During this time the library was developed from a pet project out of consideration to a full-scale neuroevolution library, designed for evolving proprietary solutions for trading on the financial markets. Many new concepts such as RTRL, Leaky integrators, HyperNEAT and Novelty Search were introduced in the following years and shown to work well in various demonstration programs published by Peter Chervenski. In 2012 NEAT Sciences's founder Shane Ryan and Peter Chervenski agreed to release the library to the public under the GNU Lesser General Public License (v 3.0) with Python bindings added.


Dependencies
============

 * boost_system


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
