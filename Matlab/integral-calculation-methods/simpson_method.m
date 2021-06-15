function result = simpson_method(a, b, N)
    result = 0;
    interval_length = (b-a)/N;
    
    for i = 1:N
       left = a + (i-1)*interval_length;
       right = a + i*interval_length;
       result = result + failure_probability(left) + 4*failure_probability((left+right)/2) + failure_probability(right);
    end
    
    result = result * interval_length/6;
end