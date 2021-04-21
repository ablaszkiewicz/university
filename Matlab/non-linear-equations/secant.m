function [result, iter_count] = secant(a, b, e, f, name)
    iter_count = 0;
    x = [];
    x_diff = [];
    while 1
        iter_count = iter_count + 1;
        m = b - (f(b) * (b - a)) / (f(b) - f(a));
        x(end+1) = m;
        
        if length(x) > 1
           x_diff(end+1) = abs(x(end) - x(end-1));
        end
        
        if abs(f(m)) < e
            result = m;
            break
        else
            a = b;
            b = m;
        end
    end
    
    myPlot(strcat(name, 'wartość.png'), 'Iteracja', 'Wartość', 1:iter_count, x);
    myPlot(strcat(name, 'różnica.png'), 'Iteracja', 'Różnica', 1:iter_count-1, x_diff);
end