# Rock-solid code demo

This repo is a demo of best practices for reliable scientific code as described in 
[a series of blog posts](http://davidketcheson.info/2015/05/12/rock_solid_code.html).

The code in this repo implements Gaussian elimination without pivoting.  Given a square matrix,
it constructs factors L and U that are lower-triangular and strictly-upper-triangular (respectively)
such that LU = A.  The algorithm is not numerically stable and should not be used for large matrices due
to the tendency for roundoff errors to be amplified.  The implementation is also very slow, since it uses
Python loops.

##Dependencies
This code requires Python and numpy.  If you have Python and pip, you can get numpy via

    pip install numpy

##Installation
To use this code, you should first copy it to your computer via

    git clone https://github.com/ketch/rock-solid-code-demo.git
    
## Usage

Then you can invoke it from the IPython prompt via

```python
    cd rock-solid-code-demo
    import factor
    import numpy as np
    A = np.random.rand(3,3)
    L, U = factor.LU(A)
```
