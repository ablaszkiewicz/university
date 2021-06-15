function result = rectangles_method(a, b, N)
    result = 0;
    interval_length = (b-a)/N;
    
    for i = 1:N
       left = a + (i-1)*interval_length;
       right = a + i*interval_length;
       result = result + failure_probability((left+right)/2)*interval_length;
    end
end