is_sum_of_three([X|T],N):-
    is_sum_of_three(T,N,X);
    is_sum_of_three(T,N).

is_sum_of_three([Y|T],N,X):-
    is_sum_of_three(T,N,X,Y);
    is_sum_of_three(T,N,X).

is_sum_of_three([Z|T],N,X,Y):-
    is_sum_of_three(T,N,X,Y,Z);
	is_sum_of_three(T,N,X,Y).

is_sum_of_three(_,N,X,Y,Z):-	
    N is X+Y+Z.
	
/*  Test Cases:
is_sum_of_three([1, 3, 5, 7],10)           should print false.
is_sum_of_three([1, 3, 5, 7],11)           should print true.
is_sum_of_three([7, 1, 10, 3, 8, 2],19)    should print true.  */