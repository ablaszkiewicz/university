function [result, iter_count] = bisection(l, r, e, f, name)
    result = 0;
    iter_count = 0;
    x = [];
    x_diff = [];
    while (true)
        iter_count = iter_count + 1;
        m = (l + r) / 2;
        current_value = f(m);
        x(end+1) = current_value;

        if length(x) > 1
            x_diff(end+1) = abs(x(end) - x(end-1));
        end
        
        if (abs(current_value) < e || abs(l - r) < e)
            result = m;
            break;
        elseif (f(l) * current_value < 0)
            r = m;
        else
            l = m;
        end
    end
    
    myPlot(strcat(name, 'wartość.png'), 'Iteracja', 'Wartość', 1:iter_count, x);
    myPlot(strcat(name, 'różnica.png'), 'Iteracja', 'Różnica', 1:iter_count-1, x_diff);
end