clc
Index = 175715;
N0 = 5;
N1 = mod(N0-1,4)+1

options = optimset('Display', 'iter');
result1 = fzero(@tan, 6, options);
result2 = fzero(@tan, 4.5, options);