# smart_calculator
A calculator, which can solve expressions with more than one operation like '24 + 5 * (2^2 -5)'


# Program's structure
1) Check whether input is correct
  - forbidden chars (&, %, abcd...)
  - incorrect scobes (like '1 + (2 + 3))')
  - incorrect operations (like '1 + 2 * - 4' or '2 + 3 * 5 -' and etc)
2) Divide expression on successive operations with recuirsive method
  - from '1 + 5 - (4 * 2^3 / 20)' to:
    1) 2^3
    2) 4 * (i)
    3) (ii) / 20
    4) 1 + 5
    5) (iv) - (iii)
3) Calculate all operations from 2 paragraph and get final result
  - as an addition save the original input expression and the calculated result

![](https://github.com/IlyaLoladze/smart_calculator/blob/main/example/Screenshot%202022-12-15%20at%2016.29.41.png)

