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

# Building project
In the terminal (./src):
```shell
python3 main.py
```
Or with bash (./example)
```shell
bash ./compile.sh
```
![](https://github.com/IlyaLoladze/smart_calculator/blob/main/example/Screenshot%202022-12-15%20at%2016.29.41.png)

# Further updates
1. Optimize the code
2. Add more detailed feedback about the incorrectness of input
3. Imrpove the algorithm (there are still cases, where it does not work properly)
4. Add shell / python script for saving the history of queries to the calculator (with info 'a wrotten expression' + 'a result from program')
