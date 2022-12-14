# smart_calculator
A calculator, which can solve expressions with more than one operation like '24 + 5 * (2^2 -5)'


# Plan
1) Check whether input is correct
  - forbidden chars (&, %, abcd...)
  - incorrect scobes (like '1 + (2 + 3))')
  - incorrect operations (like '1 + 2 * - 4' or '2 + 3 * 5 -' and etc)
2) Divide expression on successive operations
  - from '1 + 5 - (4 * 2^3 / 20)' to:
    1) 2^3
    2) 4 * (1)
    3) (2) / 20
    4) 1 + 5
    5) (4) - (3)
3) Calculate all operations from 2 paragraph and get final result
  - as an addition save the original input expression and the calculated result
