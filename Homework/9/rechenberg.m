function w=rechenberg(f,gen,popsize,std,c)
    pop = zeros(popsize,2);
    expected = 0;
    successful = 0;
    assert(c>0.817 && c<1);
    
    % Create the initial population
    for i=1:popsize
        pop(i,1)=normrnd(expected,std);
        pop(i,2)=normrnd(expected,std);
    end
    
    % Start the algorithm
    for j=1:gen
        for i=1:popsize
            % Create a new individual from the parent
            new=pop(i)+ [ normrnd(expected,std) normrnd(expected,std) ];
            % If it is better, do elitism
            if f(new(1),new(2))<f(pop(i,1),pop(i,2))
                pop(i,1)=new(1);
                pop(i,2)=new(2);
                successful = successful + 1;
            end
            % 1/5 rule
            if j==20
                ratio = successful / 20;
                if ratio > 1/5
                    std = std/c;
                elseif ratio < 1/5
                    std = std * c;
                end
            end
        end
    end
    
    % Choose the best
    r = f(pop(1,1),pop(1,2));
    point(1) = pop(1,1);
    point(2) = pop(1,2);
    for i=2:size(pop)
        if f(pop(i,1),pop(i,2))<r
            r = f(pop(i,1),pop(i,2));
            point(1)=pop(i,1);
            point(2)=pop(i,2);
        end
    end
  sprintf("(%3.2d,%3.2d,%3.2d)",point(1),point(2),r)
  
  % Plot the function and the point
  fmesh(f);
  hold on;
  plot3(point(1),point(2),r,'.b','markersize',10,'color','red');
