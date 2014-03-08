MedianFinder
============

Implementation of the randomized algorithm for median finding that 
can be found in Mitzenmacher, Upfal. Algorithm runs in linear time
and fails with probability bounded by n(-1/4), where n is the 
length of the input list.

Main method compares results for median finding using the method of
sorting the list and returning the element at index ceil(n/2). It 
also prints out the percent failure for the randomized algorithm.

TODO
=====
- Algorithm often returns bad median on small inputs. Returns correct
  median almost always on large inputs.