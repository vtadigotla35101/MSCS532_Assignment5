# MSCS532_Assignment5
QuickSort Implementation, Analysis &amp; Randomization.

How to Run the Code:
1.Open a terminal or command prompt.
2.Navigate to the directory where you saved your file.
3.Run the script using the following command: 
    Command: python quicksort_analysis.py

You will see the output printed directly to your terminal, showing the performance comparison for each data type and size. It might take a few moments to complete, especially for the larger, sorted arrays running on the deterministic algorithm.


Summary of Findings:
1.Random Data: As predicted by the theoretical analysis, both deterministic and randomized Quicksort perform exceptionally well on random data. Their running times are nearly identical and scale in a way that is consistent with O(nlogn) growth.
2.Sorted & Reverse-Sorted Data: The results here are stark and perfectly illustrate the core problem of a fixed-pivot strategy.
  a.The deterministic Quicksort slows down dramatically. The runtime grows quadratically (O(n2)), as seen by the huge jump in time when n doubles. For n=9999, it takes over 5 seconds, whereas it took only milliseconds for the random array of the same size. This is the worst-case scenario in action.
  b.The randomized Quicksort, in contrast, shows no performance degradation. Its runtime on sorted and reverse-sorted data is virtually identical to its runtime on random data. By randomly selecting a pivot, it avoids the pitfall of consistently picking the worst element and maintains its expected O(nlogn) performance.

This empirical analysis provides clear, practical evidence for the theoretical concepts. It demonstrates that while Quicksort is an extremely fast algorithm on average, the deterministic version is vulnerable to common data patterns. Randomization is a simple but powerful technique to fortify the algorithm against these vulnerabilities, making it a robust and reliable choice for general-purpose sorting
