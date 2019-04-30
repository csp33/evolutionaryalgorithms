% Declare the function
syms x y;
f(x,y)=100*(y-x^2)^2+(x-1)^2;
% Calculate the derivatives
d1x=diff(f,x);
d1y=diff(f,y);
d11x=diff(d1x,x);
% Find the critical point(s)
[a,b]=solve(d1x,d1y);
% Build the Hessian matrix
H=hessian(f,[x,y]);
% Calculate the determinant
dH=det(H);
% Test the critical point on it
r = dH(a,b);
if r > 0
    if d11x(a,b) > 0
        sprintf("%d,%d is a local minimum",a,b)
    elseif d11x(a,b)<0
        sprintf("%d,%d is a local maximum",a,b)
    end
elseif r == 0
    sprintf("We can not determine anything about %d,%d",a,b)
else
    sprintf("%d,%d is a saddle point",a,b)
end

%CURVATURE
% Get the Hessian matrix evaluated on the point
h = H(a,b);
A=size(h);
principal_minors=(1:1:A);
B=A(1:1);
for k=(1:B)
x=h(1:k,1:k);
C=det(x);
principal_minors(1,k)=C;
end
if all(principal_minors>0)
   sprintf("The function is strictly convex")
elseif  all(principal_minors>=0)
    sprintf("The function is convex")
elseif all(principal_minors<0)
    sprintf("The function is strictly concave")
elseif all(principal_minors<=0)
    sprintf("The function is concave")
else
    sprintf("We can not determine the curvature of the function")
end