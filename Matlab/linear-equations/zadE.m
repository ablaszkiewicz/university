clc
clear all
close all
Index=175715
N0=5
N1=mod(N0-1,4)+1

density = 10;
d = 0.85;
Ns = [500, 1000, 3000, 6000, 12000];

for i=1:length(Ns)
    N = Ns(i);
    [Edges] = generate_network(N, density);

    I = speye(N);
    A = sparse(N,N);
    b = repmat((1-d)/N, N,1);
    edges_size = size(Edges);
    Ones = ones(1, edges_size(2));
    B = sparse(Edges(2, :), Edges(1, :), Ones);

    for j = 1:height(A)
       A(j,j) = 1/sum(B(:,j));
    end
    M = I - d*B*A;
    r = ones(N,1);
    L = tril(M,-1);
    U = triu(M,1);
    D = diag(diag(M));

    minNorm = 10^-14;
    currentNorm = Inf;
    iter = 0;

    % zadanie różnicujące
    tic
    inv(sparse(D) + sparse(L));
    inversionTimes(i) = toc;

    left =  mldivide(-D, L + U);
    right = mldivide(D, b);

    tic
    if N == 1000
        while currentNorm > minNorm
           iter = iter + 1;
           r = left * r + right;
           res = M*r - b;
           currentNorm = norm(res);
           norms(iter) = currentNorm;
        end
    else
        while currentNorm > minNorm
           iter = iter + 1;
           r = left * r + right;
           res = M*r - b;
           currentNorm = norm(res);
        end
    end
    
    
    iterations(i) = iter;
    times(i) = toc;
end

iterations
times

plot(Ns, times);
title('Jacobi solve time');
xlabel('N');
ylabel('Time [s]');
saveas(gcf, "zadE_175715_0.png");

plot(Ns, iterations);
title('Jacobi iterations');
xlabel('N');
ylabel('Number of iterations');
saveas(gcf, "zadE_175715_1.png");

semilogy(norms, [1:length(norms)]);
title('Jacobi norms');
xlabel('N');
ylabel('Norm');
saveas(gcf, "zadE_175715_2.png");

plot(inversionTimes, Ns);
title('D+L inversion time');
xlabel('Size');
ylabel('Time [ms]');
saveas(gcf, "zadE_175715_3.png");