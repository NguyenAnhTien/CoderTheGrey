# Knuth-Morris-Pratt

The basic idea behind the algorithm is:
whenever we detect a mismatch, we already know some of the characters in the text.
Since they matched the pattern characters prior to the mismatch.
We can take advantage of this information to avoid backing up the text pointer over
all those known characters.
