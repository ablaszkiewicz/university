clc
clear all
close all
Index=175715
N0=5
N1=mod(N0-1,4)+1

Ns = [500, 1000, 3000, 6000, 12000];

for i = 1:5
tic
N = Ns(i)

%------- OBLICZENIA --------
d = 0.85;
density = 3;
disp("Generating network");
[Edges] = generate_network(N, density);
disp("Generating matrixes");

I = speye(N);
A = sparse(N,N);
b = repmat((1-d)/N, N,1);

edges_size = size(Edges)
Ones = ones(1, edges_size(2));
B = sparse(Edges(2, :), Edges(1, :), Ones);

disp("For");
for j = 1:height(A)
   A(j,j) = 1/sum(B(:,j));
end
disp("Counting M");
M = I - d*B*A;
disp("Counting r");
r = M\b;
%---------------------------
elapsed = toc
czas_Gauss(i) = elapsed
end

plot(Ns, czas_Gauss);
title("Czas bezpośredniego rozwiązania")
xlabel("N")
ylabel("Czas")
saveas(gcf, "zadD_175715.png");