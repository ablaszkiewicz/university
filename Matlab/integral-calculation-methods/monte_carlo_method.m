function result = monte_carlo_method(a, b, N)
    result = 0;
    interval_length = (b-a)/N;
    
    values = zeros(1,N);
    
    for i = 1:N
        values(i) = failure_probability(a + (i-1)*interval_length);
    end
    
    min_y = min(values);
    max_y = max(values);
    full_y = max_y - min_y;
    
    min_x = a;
    max_x = b;
    full_x = b - a;
    
    points_hit = 0;
    
    for i = 1:N
        x = rand() * full_x + min_x;
        y = rand() * full_y + min_y;
        
        function_value = failure_probability(x);
        
        if y > min_y && y < function_value
            points_hit = points_hit + 1;
        end
    end
    
    result = points_hit / N * full_y * full_x;
end