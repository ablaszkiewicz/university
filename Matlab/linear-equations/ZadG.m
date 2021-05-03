clc
clear all
close all
Index=175715
N0=5
N1=mod(N0-1,4)+1

load('Dane_Filtr_Dielektryczny_lab3_MN.mat')
N = length(M);

% bezpośrednia metoda
display('Bezpośrednia')
r1 = M\b;

% Jacobi
display('Jacobi')
r2 = ones(N,1);
L = tril(M,-1);
U = triu(M,1);
D = diag(diag(M));

minNorm = 10^-14;
currentNorm = Inf;
iter = 0;

left =  mldivide(-D, L + U);
right = mldivide(D, b);

while currentNorm > minNorm
   iter = iter + 1;
   r2 = left * r2 + right;
   res = M*r2 - b;
   currentNorm = norm(res);
end

% Gauss-Seidel
display('Gauss-Seidel')
r3 = ones(N,1);
L = tril(M,-1);
U = triu(M,1);
D = diag(diag(M));

minNorm = 10^-14;
currentNorm = Inf;
left =  -(D + L) \ U * r3;
right = (D + L) \ b;
iter = 0;

while currentNorm > minNorm
   iter = iter + 1;
   left =  mldivide(-(D + L),U * r3);
   r3 = left + right;
   res = M*r3 - b;
   currentNorm = norm(res);
end