clc
Index = 175715;
N1 = 5;
N2 = 1;

n_max = 10000;
a = 1;
b = 1;
r_max = 0.2;

X = zeros(1, n_max);
Y = zeros(1, n_max);
R = zeros(1, n_max);
rand_no = zeros(1, n_max);
rand_no_avg = zeros(1, n_max);

surfaces = zeros(1, n_max);
total_surface = zeros(1, n_max);

tiledlayout(2,2)
nexttile
hold on
axis equal


for i = 1:n_max
    intersection = true;
    while intersection
        rand_no(i) = rand_no(i)+1;
        temp_r = rand*r_max;
        temp_x = rand*(a-2*temp_r) + temp_r;
        temp_y = rand*(b-2*temp_r) + temp_r;
        
        if i == 1
            intersection = false;
        end
        
        for j = 1:i-1
            if sqrt( (temp_x-X(j))^2 + (temp_y-Y(j))^2 ) < temp_r + R(j)
                intersection = true;
                break;
            else
                intersection = false;
            end
            
        end
    end
    plot_circ(temp_x, temp_y, temp_r);
    X(i) = temp_x;
    Y(i) = temp_y;
    R(i) = temp_r;
    surfaces(i) = pi*temp_r*temp_r;
    rand_no_avg = cumsum(rand_no)./[1:n_max];
end
hold off
title("Pęcherzyki")

nexttile
semilogx([1:n_max], rand_no_avg)
title("Średnia liczba losowań")
xlabel("Iteracja")
ylabel("Losowania")

nexttile
loglog([1:n_max], cumsum(surfaces)./(a*b))
title("Procent wypełnienia")
xlabel("Iteracja")
ylabel("Wypełnienie")

function plot_circ(X, Y, R)
theta = linspace(0,2*pi);
x = R*cos(theta) + X;
y = R*sin(theta) + Y;
plot(x,y)
end