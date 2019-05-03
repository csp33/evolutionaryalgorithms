function r=gradient_method(f,initial,lr,iterations)
    % Gradient method
    syms x y;
    previous = initial;
    current = initial;
    grad = [ diff(f,x) diff(f,y) ];
    for i=1:iterations
        current = previous + lr * (-grad(previous(1),previous(2)));
        previous = current;
    end
    value = f(current(1),current(2));
    sprintf("Minimum at (%f,%f) = %f",current(1),current(2),value)
    % Plot the function and the point
    fmesh(f);
    hold on;
    plot3(current(1),current(2),value,'.b','markersize',10,'color','red');