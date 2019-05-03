function r = r_grad(x,y)
    r = [ 2*x - 400*x*(- x^2 + y) - 2, - 200*x^2 + 200*y];