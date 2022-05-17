# Knuth-Morris-Pratt

The basic idea behind the algorithm is:
whenever we detect a mismatch, we already know some of the characters in the text.
Since they matched the pattern characters prior to the mismatch.
We can take advantage of this information to avoid backing up the text pointer over
all those known characters.

## Example
A B A A A A B A A A A A A A A A
  B A A A A A A A A A

Notice that this is two-character alphabet string.
When the mismatch is detected, we know that the six previous characters in the text must
be B A A A A A A A A B.
The text pointer now pointing at the B at the end.
The key observation is that we need not back up the text pointer **i**, since the previous four
in the text are all **A**s and do not match the first character in the pattern.

The character currently pointed to by **i** is as B

The insight of the KMP algorithm is that we can decide ahead of time exactly how to restart the search, because that decision depends only on the pattern. 

## Backing up the pattern pointer
In KMP sub- string search, we never back up the text pointer **i**.
use an array dfa[][] to record how far to back up the pattern pointer j when a mismatch is detected.
