function [fitn, endpop]=backpack_elitista(weights,values,...
    capacity,probofcrossover,probofmutation,generations,populationsize,...
    tournamentsize)


% Initial population:
numberofitems=length(weights); 
endpop=ceil(rand(populationsize,numberofitems)-0.5);  


fitn=zeros(populationsize, generations);

for i=1:generations 
    
    populaciofitness=fitness(endpop,weights,values,capacity);
    fitn(:,i)=populaciofitness;
    [~, elitpos]=max(populaciofitness);
    elitindividual=endpop(elitpos, :);
    endpop=selection_tournament(endpop,populaciofitness,tournamentsize);
    endpop=crossover_onepoint(endpop,probofcrossover);
    endpop=mutation_onebit(endpop,probofmutation);
    endpop(1,:)=elitindividual;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function populationfitness=fitness(population,weights,values,capacity)

populationfitness=zeros(size(population,1),1); 

for i=1:size(population,1)
    
    if dot(population(i,:),weights)>capacity
        populationfitness(i)=0;
    else
        populationfitness(i)=dot(population(i,:),values);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function parents=selection_tournament(population,populationfitnes,tournamentsize)

parents=zeros(size(population));

for i=1:size(population,1)
    positions=ceil(size(population,1)*rand(tournamentsize,1));
    [~,bestpos]=max(populationfitnes(positions));
    parents(i,:)=population(positions(bestpos),:);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function offspring=crossover_onepoint(population,probofcrossover)

offspring=population;
n=size(population,2);

for i=1:2:size(population,1)

    if rand<probofcrossover
    
        breakpoint=ceil((n-1)*rand);
        offspring(i,:)=[population(i,1:breakpoint), population(i+1,breakpoint+1:n)];
        offspring(i+1,:)=[population(i+1,1:breakpoint), population(i,breakpoint+1:n)];
    else
        offspring(i,:)=population(i,:); 
        offspring(i+1,:)=population(i+1,:);
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%555

function offspring=mutation_onebit(population,probofmutation)

offspring=population;

n=size(population,2);

for i=1:size(population,1)
    if rand<probofmutation 
        position=ceil(n*rand); 
        if population(i,position)==0
            offspring(i,position)=1; 
        else
            offspring(i,position)=0;
        end
    end
end
