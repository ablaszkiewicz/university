clc
Index = 175715;
N0 = 5;
N1 = mod(N0-1,4)+1

[result1_bisection, iter_count1_bisection] = bisection(1, 60000, 1e-3, @func1, "bisekcja1");
[result1_secant, iter_count1_secant] = secant(1, 60000, 1e-3, @func1, "sieczne1");

[result2_bisection, iter_count2_bisection] = bisection(0, 50, 1e-12, @func2, "bisekcja2");
[result2_secant, iter_count2_secant] = secant(0, 50, 1e-12, @func2, "sieczne22");

[result3_bisection, iter_count3_bisection] = bisection(0, 50, 1e-12, @func3, "bisekcja3");
[result3_secant, iter_count3_secant] = secant(0, 50, 1e-12, @func3, "sieczne3");

function result = func1(N)
    result = (N.^1.43 + N.^1.14) / 1000 - 5000;
end
function result = func2(omega)
    R = 725;
    C = 8*1e-5;
    L = 2;
    result = 1 / (sqrt( 1/R.^2 + (omega * C - 1 / (omega * L)).^2)) - 75
end
function result = func3(t)
    g = 1.622;
    m0 = 150000;
    q = 2700;
    u = 2000;
    result = u * log(m0 / (m0 - q * t)) - g * t - 750;
end