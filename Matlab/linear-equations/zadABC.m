clc
clear all
close all
Index=175715
N0=5
N1=mod(N0-1,4)+1

d = 0.85;
N = 10;
density = 3; % parametr decyduj�cy o gestosci polaczen miedzy stronami
[Edges] = generate_network(N, density);

I = speye(N);
B = sparse(N,N);
A = sparse(N,N);
b = repmat((1-d)/N, N,1);

save zadB_175715 A B I b

for i = Edges
    B(i(2), i(1)) = 1;
end

for i = 1:height(A)
   A(i,i) = 1/sum(B(:,i));
end

M = I - d*B*A;
r = M\b