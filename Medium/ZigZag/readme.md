**Zigzag Conversion**

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

Example 2:

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

Explanation:

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

Example 3:

```
Input: s = "A",
numRows = 1
Output: "A"
``` 

Constraints:

```
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
```

Solution:

**Intuition**

The intuition is to create the zigzag pattern by placing each character of the input string in the appropriate row. We
will be moving up and down through the rows to simulate the zigzag pattern.

**Approach**

1. We handle the base cases: when numRows is 1 or the length of the input string is less than or equal to numRows, we
   don't need to create a zigzag pattern, so we return the original string.
2. We create a list called 'rows' containing numRows empty strings, where each string represents a row in the zigzag
   pattern.
3. We initialize a variable 'row' to keep track of the current row while iterating through the input string.
4. We use a boolean variable 'going_down' to determine the direction of movement in the zigzag pattern.
5. We iterate through each character in the input string, appending it to the corresponding row in 'rows'.
6. When we reach the top or bottom row (row == 0 or row == numRows - 1), we reverse the direction by toggling '
   going_down'.
7. After processing all characters, we join the rows into a single string using the 'join' method and return the result.

**Complexity**

Time complexity:
O(n), where n is the length of the input string 's'. We iterate through each character once.

Space complexity:
O(n), we use additional space to store the 'rows' list, which has a size proportional to the length of the input string.