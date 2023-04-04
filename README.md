# IR-with-LSH

We have implemented the LSH algorithm to build a search engine. Then did a comparative analysis for different 50, 100, and 200 hash functions. For each value, output the pairs that have an estimated similarity at least 0.5, and report the number of false positives and false negatives that you obtain. For the false positives and negatives, report the averages for 5 different runs.

Next, break up the signature table into b bands with r hash functions per band and implement Locality Sensitive Hashing. The goal is to find candidate pairs with similarity at least 0.6. Experiment with r=5, b =10 for the table with the 50 hash functions, r=5, b=20 for the table with the 100 hash functions, r = 5, b = 40 and r=10, b= 20 for the table with the 200 hash functions.
