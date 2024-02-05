f = @(x) 14*x*exp(x-2)-12*exp(x-2)-7*x^3+20*x^2-26*x+12

x_values = linspace(0,3,1000);
y_values = arrayfun(f,x_values);

figure;

plot(x_values, y_values);
title ('Γραφική Παράσταση της f');
xlabel('x');
ylabel('f(x)');
grid on ; 

saveas(gcf,'ex1_grapgh.png');


