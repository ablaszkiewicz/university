clc
clear all
close all
SSID = 175715;

% odpowiednie fragmenty kodu mo�na wykona� poprzez znazaczenie i wci�ni�cie F9
% komentowanie/ odkomentowywanie: ctrl+r / ctrl+t

% Zadanie A
%------------------
d = 0.85;
N = 10;
density = 3; % parametr decyduj�cy o gestosci polaczen miedzy stronami
[Edges] = generate_network(N, density);
%-----------------

% Zadanie B
%------------------
% generacja macierzy I, A, B i wektora b
I = speye(N);
B = sparse(N,N);
A = sparse(N,N);
b = repmat((1-d)/N, N,1);

save zadB_175715 A B I b
%-----------------

% Zadanie C
%-----------------
for i = Edges
    B(i(2), i(1)) = 1;
end

for i = 1:height(A)
   A(i,i) = 1/sum(B(:,i));
end

M = I - d*B*A;
r = M\b

%-----------------

% Zadanie D
%------------------
clc
clear all
close all

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
B = [N,N];
A = sparse(N,N);
b = repmat((1-d)/N, N,1);
disp("First for");
for j = Edges
    B(j(2), j(1)) = 1;
end
disp("Second for");
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
%------------------



% Zadanie E
%------------------
clc
clear all
close all

% przyk�ad dzia�ania funkcji tril, triu, diag:
% Z = rand(4,4)
% tril(Z,-1) 
% triu(Z,1) 
% diag(diag(Z))


for i = 1:5
tic
% obliczenia
czas_Jacobi(i) = toc;
end

plot(N, czas_Jacobi)
%------------------