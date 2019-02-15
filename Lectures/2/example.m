numberofitems=30;
weights=ones(1, numberofitems);
weights(2:2:end)=10;

values=ones(1, numberofitems);
values(1:2:end)=10;

capacity=numberofitems*2.5;
% The value of optimal packing is 5.2*n (156 for 30 items)
generation=100;
populationsize=30;
probofcrossover=0.9;
probofmutation=0.01;

[fit, endpop] = backpack_elitista(weights,values,capacity,...
    probofcrossover, probofmutation, generation, populationsize,4);
endpop(1,:)
max(max(fit))
plot(1:generation, sum(fit)/populationsize,'b', 1:generation, max(fit,[],1),'g' )
xlabel('Generation')
ylabel('Fitness')