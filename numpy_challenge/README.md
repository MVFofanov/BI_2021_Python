# Description

This is my NumPy challenge!

## Usage

Available commands: | Input: | Output:
------------ | ------------- | -------------
matrix multiplication (mmul) | two matrices | product matrix
multiplication check (mc) | matrix list | boolean test result of matrices possibility to be multiplied
multiply matrices (mmat) | matrix list | multiplication matrices product
compute 2d distance (c2dd) | two arrays (1 dimension) | calculated distance between these points coordinates
compute multidimensional distance (cmd) | two arrays (1 dimension) | calculated distance between these arrays
compute pair distances (cpd) | one array (2 dimension) | paired distance matrix


Functions have the same names as commands above with only space (' ') replaced with the underscore character ('_')
Commands can be used via its short forms indicated in the brackets in the first column

Type "exit", "quit", "e" or "q" to quit the program

## Examples:

### Matrix multiplication:

#### Input:
```
Type your command: matrix multiplication
Type your two arrays
Type your array, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9
Type your array, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9
```

#### Output:
```
[[ 61  62  84]
 [ 29  29  39]
 [103 109 150]]
```

### Multiplication check:

#### Input:
```
Type your command: multiplication check
Type your matrix list, matrices should be separated with spaces, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9 3,4,6;1,2,3;8,7,9
```

#### Output:
```
True
```

#### Input:
```
Type your command: multiplication check
Type your matrix list, matrices should be separated with spaces, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9 2,4,3,6
```

#### Output:
```
False
```

### Multiply matrices:

#### Input:
```
Type your command: multiply matrices
Type your matrix list, matrices should be separated with spaces, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9 3,4,6;1,2,3;8,7,9 3,4,6;1,2,3;8,7,9 3,4,6;1,2,3;8,7,9
```

#### Output:
```
[[14171 14736 20142]
 [ 6627  6890  9417]
 [24894 25897 35403]]
```

#### Input:
```
Type your command: multiply matrices
Type your matrix list, matrices should be separated with spaces, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9 4,5;7,8
```

#### Output:
```
None
```

### Compute 2d distance:

#### Input:
```
Type your command: compute 2d distance
Type your two arrays
Type your array, columns should be separated with commas while rows with semicolons: 0,3
Type your array, columns should be separated with commas while rows with semicolons: 4,0
```

#### Output:
```
5.0
```

#### Input:
```
Type your command: compute 2d distance
Type your two arrays
Type your array, columns should be separated with commas while rows with semicolons: 0,3,4
Type your array, columns should be separated with commas while rows with semicolons: 4,0,5
```

#### Output:
```
This arrays are not 2d!
```

### Compute multidimensional distance:

#### Input:
```
Type your command: compute multidimensional distance
Type your two arrays
Type your array, columns should be separated with commas while rows with semicolons: 0,3,4
Type your array, columns should be separated with commas while rows with semicolons: 4,0,5
```

#### Output:
```
5.0990195135927845
```

### Compute pair distances:

#### Input:
```
Type your command: compute pair distances
Type your array, columns should be separated with commas while rows with semicolons: 3,4,6;1,2,3;8,7,9
```

#### Output:
```
[[ 0.          4.12310563  6.55743852]
 [ 4.12310563  0.         10.48808848]
 [ 6.55743852 10.48808848  0.        ]]
```
