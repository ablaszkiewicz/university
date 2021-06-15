clc
clear all
close all

load dane_jezioro
surf(XX,YY,FF)
shading interp
axis equal

N = 1e5;
points_hit = 0;

for i = 1:N
   x = rand() * 100;
   y = rand() * 50 - 50;
   z = rand() * 100;
   
   depth = glebokosc(x, z);
   
   if y > depth
      points_hit = points_hit + 1;
   end
end

V = points_hit / N * (100*100*50)