# mathsq
Math sequence. Useful for calculations.

> [!NOTE]
> This uses basic math and is incompatible with array frameworks like NumPy. We strive to keep it light.

```python
from mathsq import MathSQ

array = MathSQ(
  a1=10,  # first item
  d=2,    # common difference
  ln=10   # length ($n$ sequence)
)
```
This yields a sequence:

$$
\( a_n \): 10, 12, 14, \ldots
$$

We can also create a `MathSQ` from specifying the $`n`$-th element.

```python
array = MathSQ.from_n_assignment(
  n=10,
  value=100,
  d=-1
)
```

## Set array length
This returns the array itself.

```python
>>> array = array.setln(100)
```

## Get $`n`$-th element
> [!NOTE]
> Out-of-bounds are not handled.

```python
>>> array.n(5)
```

## Get $`n`$ from value
> [!NOTE]
> Out-of-index is not handled.

```python
>>> array.n_of(10)
```

## Get middle $`n`$
> [!NOTE]
> May return a `float`.

```python
>>> array.mid_n()
```

## Get middle value
> [!NOTE]
> Out-of-bounds are not handled.

```python
>>> array.mid()
>>> # ...or
>>> array.M
```

## Has middle?
Returns `True` if the middle index exists.

```python
>>> array.has_mid()
```

## Sum

```python
>>> array.sum()
>>> # ...or
>>> array.S
```

## Basic manipulations

> [!NOTE]
> Implementation not fully covered.

```python
>>> array1 = array0 + 10 # array +/- float
>>> array1 -= array0 # array +/- array
>>> array1.a1
10

>>> array1 * 10
```


