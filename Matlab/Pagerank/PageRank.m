%moja sieć miała już link 6 jako najpopularniejszy, więc jako modyfikację
%dodałem jedno dodatkowe połączenie 1 -> 2

clc
Index = 175715;
N1 = 5;
N2 = 1;
Z = 1+mod(N1,7)

edges = [1,1,1,2,2,2,3,4,4,5,5,6,6,7;
         4,6,2,3,4,5,6,5,6,4,6,4,7,6];
     
d = 0.85;
N = 7;

I = eye(N);
B = sparse(N,N);
A = sparse(N,N);
b = repmat((1-d)/N, N,1);


for i = edges
    B(i(2), i(1)) = 1;
end

for i = 1:height(A)
   A(i,i) = 1/sum(B(:,i));
end

M = I - d*B*A;
r = M\b
 


bar(r)
nnz(B)