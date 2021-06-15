clc
clear all
close all

load P_ref

reference_value = P_ref

Ns = 5:50:1e4;
rectangles_method_values = zeros(1, length(Ns));
trapezoids_method_values = zeros(1, length(Ns));
simpson_method_values = zeros(1, length(Ns));
monte_carlo_method_values = zeros(1, length(Ns));

for i = 1:length(Ns)
    N = Ns(i);
    rectangles_method_values(i) = abs(reference_value - rectangles_method(0, 5, N));
    trapezoids_method_values(i) = abs(reference_value - trapezoids_method(0, 5, N));
    simpson_method_values(i) = abs(reference_value - simpson_method(0, 5, N));
    monte_carlo_method_values(i) = abs(reference_value - monte_carlo_method(0, 5, N));
end

N = 1e7;
times = zeros(4, 1);
tic
rectangles_method(0, 5, N);
times(1) = toc;

tic
trapezoids_method(0, 5, N);
times(2) = toc;

tic
simpson_method(0, 5, N);
times(3) = toc;

tic
monte_carlo_method(0, 5, N);
times(4) = toc;

loglog(Ns, rectangles_method_values)
title("Metoda prostokątów")
xlabel("Liczba przedziałów")
ylabel("Błąd bezwzględny")
saveas(gcf, 'rectangles_method_error.png')

loglog(Ns, trapezoids_method_values)
title("Metoda trapezów")
xlabel("Liczba przedziałów")
ylabel("Błąd bezwzględny")
saveas(gcf, 'trapezoids_method_error.png')

loglog(Ns, simpson_method_values)
title("Metoda simpsona")
xlabel("Liczba przedziałów")
ylabel("Błąd bezwzględny")
saveas(gcf, 'simpson_method_error.png')

loglog(Ns, monte_carlo_method_values)
title("Metoda monte carlo")
xlabel("Liczba przedziałów")
ylabel("Błąd bezwzględny")
saveas(gcf, 'monte_carlo_method_error.png')

x = categorical({'Prostokąty','Trapezy','Simpson','Monte-Carlo'});
x = reordercats(x,{'Prostokąty','Trapezy','Simpson','Monte-Carlo'});
bar(x, times)
title("Porównanie czasu poszczególnych metdod")
ylabel("Czas [s]")
saveas(gcf, 'comparison.png')
