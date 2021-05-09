clear
clc
Index = 175715;
N0 = 6;
N1 = mod(N0-1,4)+1;

iterations = 45

Ks = linspace(1, iterations, iterations);

FF = 0;
for i = 1:length(Ks)
    
    K = Ks(i);
    [x, y, f] = lazik(K);
    [XX, YY] = meshgrid(linspace(0, 100, 101), linspace(0, 100, 101));

    if i == 0
       FF_old = 0;
    else
       FF_old = FF;
    end
    
    % polyfit
    [p] = polyfit2d(x, y, f);
    [FF] = polyval2d(XX, YY, p);
    
    
    Div_K(i) = max(max(abs(FF - FF_old)));
end

subplot(2,1,1);
plot(1:iterations, Div_K);
title("Zbieżność przy wielomianowej interpolacji");
ylabel("Maksymalna różnica");
xlabel("Iteracja");

for i = 1:length(Ks)
    
    K = Ks(i);
    [x, y, f] = lazik(K);
    [XX, YY] = meshgrid(linspace(0, 100, 101), linspace(0, 100, 101));

    if i == 0
       FF_old = 0;
    else
       FF_old = FF;
    end
    
    % polyfit
    [p] = trygfit2d(x, y, f);
    [FF] = trygval2d(XX, YY, p);
    
    
    Div_K(i) = max(max(abs(FF - FF_old)));
end

subplot(2,1,2);
plot(1:iterations, Div_K);
title("Zbieżność przy trygonometrycznej interpolacji");
ylabel("Maksymalna różnica");
xlabel("Iteracja");