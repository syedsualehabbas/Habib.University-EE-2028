% Plotting 1st function 
subplot (3,1,1) %1st 
plot x=-3:1:3;
m = x.^2; 
plot(x,m,'k','LineWidth',2.5)
title('Plotting m(x)');
xlabel('x'); 
ylabel('Amplitude');

% Plotting 2nd function 
subplot (3,1,2) 
plot x=-3:0.1:3;
n = 2.5*(x.^2);
plot(x, n,'r')
title('Plotting n(x)');
xlabel('x'); 
ylabel('Amplitude');

% Plotting 3rd function 
subplot (3,1,3) 
plot x=-5:0.01:5;
p = 2*(x.^2); 
plot(x, p,'g*')
title('Plotting p(x)');
xlabel('x');
ylabel('Amplitude');

% Adding main/super title
suptitle ('Non-linear graphs') %ignore this command if gives error
