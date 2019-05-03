% Gradient method
syms x y;
f(x,y)=100*(y-x^2)^2+(x-1)^2;
initial = [ 6 6 ];
iterations = 10000000;
lr = 0.0001;
previous = initial;
current = initial;
for i=1:iterations
    current = previous + lr * (-r_grad(previous(1),previous(2)));
    previous = current;
end
value = f(current(1),current(2));
sprintf("Minimum at (%f,%f) = %f",current(1),current(2),value)
% Plot the function and the point
fmesh(f);
hold on;
plot3(current(1),current(2),value,'.b','markersize',10,'color','red');