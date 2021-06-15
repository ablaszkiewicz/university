function result = failure_probability(t)
    o = 3;
    u = 10;
    result = 1 / (o*sqrt(2*pi)) * exp(-(t-u)^2 / (2*o^2));
end