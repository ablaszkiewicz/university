clc
clear all
close all

Index = 175715
N0 = mod(Index,10);
N1 = mod(N0-1,4)+1;

% ------ TASK 2 ------
load trajektoria1.mat

plot3(x,y,z,'o');
grid on;
axis equal;
title("Drone flight trajectory");
xlabel("x");
ylabel("y");
zlabel("z");

% ------ TASK 3 ------
N = 50;

[~, x_approximated] = aproksymacjaWiel(n, x, N);
[~, y_approximated] = aproksymacjaWiel(n, y, N);
[~, z_approximated] = aproksymacjaWiel(n, z, N);
plot3(x_approximated, y_approximated, z_approximated,'LineWidth',4, 'color', 'black');

% ------ TASK 4 ------
hold on
grid on;
axis equal;
title("Real and approximated trajectory (poly)");
xlabel("x");
ylabel("y");
zlabel("z");
plot3(x, y, z,'o', 'color', 'blue');
plot3(x_approximated, y_approximated, z_approximated,'LineWidth', 4, 'color', 'black');
hold off;

% ------ TASK 5 ------
load trajektoria2.mat
N = 62;
[~, x_approximated] = aproksymacjaWiel(n, x, N);
[~, y_approximated] = aproksymacjaWiel(n, y, N);
[~, z_approximated] = aproksymacjaWiel(n, z, N);
plot3(x_approximated, y_approximated, z_approximated,'LineWidth',4, 'color', 'black');

err = [];
M = length(n)

for N = 1:71
    [~, x_approximated] = aproksymacjaWiel(n, x, N);
    [~, y_approximated] = aproksymacjaWiel(n, y, N);
    [~, z_approximated] = aproksymacjaWiel(n, z, N);
    
    err_single = (sqrt(sum(x - x_approximated).^2) + sqrt(sum(y - y_approximated).^2) + sqrt(sum(z - z_approximated).^2)) / M;
    
    err = [err, err_single];
end

semilogy(err)
title("Poly approximation error (1 .. 71)");
xlabel("N");
ylabel("Error");

% ------ TASK 6 ------
[x_approximated] = aprox_tryg(n, x, N);
[y_approximated] = aprox_tryg(n, y, N);
[z_approximated] = aprox_tryg(n, z, N);
% zastosowałem aproksymację, ale w poleceniu nie ma żadnych informacji, co
% mam z nią zrobić, dlatego też zrobię po prostu wykres

hold on
grid on;
axis equal;
title("Real and approximated trajectory (tryg)");
xlabel("x");
ylabel("y");
zlabel("z");
plot3(x, y, z,'o', 'color', 'blue');
plot3(x_approximated, y_approximated, z_approximated,'LineWidth', 4, 'color', 'black');
hold off;

% ------ TASK 7 ------

N = 62;

[x_approximated] = aprox_tryg(n, x, N);
[y_approximated] = aprox_tryg(n, y, N);
[z_approximated] = aprox_tryg(n, z, N);
plot3(x_approximated, y_approximated, z_approximated,'LineWidth',4, 'color', 'black');
title("Tryg approximation for N=62")

err = [];
M = length(n)

for N = 1:71
    [x_approximated] = aprox_tryg(n, x, N);
    [y_approximated] = aprox_tryg(n, y, N);
    [z_approximated] = aprox_tryg(n, z, N);
    
    err_single = (sqrt(sum(x - x_approximated).^2) + sqrt(sum(y - y_approximated).^2) + sqrt(sum(z - z_approximated).^2)) / M;
    
    err = [err, err_single];
end

semilogy(err)
title("Tryg approximation error (1 .. 71)");
xlabel("N");
ylabel("Error");


