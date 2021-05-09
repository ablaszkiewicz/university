clear
clc
Index = 175715;
N0 = 6;
N1 = mod(N0-1,4)+1;

Ks = [3,7,13,37]

for i = 1:length(Ks)
    K = Ks(i)
    [x, y, f] = lazik(K)
    [XX, YY] = meshgrid(linspace(0, 100, 101), linspace(0, 100, 101))

    % path
    subplot(2, 2, 1);
    plot(x, y, '-o');
    title("Trasa łazika");
    ylabel("Y[m]");
    xlabel("X[m]");
    
    % read points
    subplot(2, 2, 2)
    plot3(x, y, f, '.');
    title("Bezpośredni odczyt");
    ylabel("Y[m]");
    xlabel("X[m]");
    zlabel("Stopień radiacji [Sv]");
    
    % polyfit
    [p] = polyfit2d(x, y, f);
    [FF] = polyval2d(XX, YY, p);
    subplot(2, 2, 3);
    surf(XX, YY, FF);
    shading flat;
    title("Interpolacja wielomianowa");
    ylabel("Y[m]");
    xlabel("X[m]");
    zlabel("Zinterpolowany stopień radiacji [Sv]");
    
    % trygfit
    [p] = trygfit2d(x, y, f);
    [FF] = trygval2d(XX, YY, p);
    subplot(2, 2, 4);
    surf(XX, YY, FF);
    shading flat;
    title("Interpolacja trygonometryczna");
    ylabel("Y[m]");
    xlabel("X[m]");
    zlabel("Zinterpolowany stopień radiacji [Sv]");
    pause()
end