:- ensure_loaded("pokemon_list.pl").
:- ensure_loaded("pokemon_info_attacks.pl").
:- ensure_loaded("pokemon_route.pl").

player_starts(0,0).

% --- AUXILIAR: at_index (A tua versão sem nth0) ---
% Caso base: o índice é 0, o elemento que queremos é a cabeça da lista.
at_index(0, [Elemento|_], Elemento).

% Caso recursivo: o índice é N, ignoramos a cabeça e procuramos N-1 no resto.
at_index(N, [_|Resto], Elemento) :-
    N > 0,
    N1 is N - 1,
    at_index(N1, Resto, Elemento).

% --- PREDICADO PRINCIPAL: next_rooms ---
next_rooms(X, Y, Rooms) :-
    % O findall tem de estar DENTRO do corpo do next_rooms
    findall([Id, Name, Level, NX, NY, Types],
        (
            % 1. Define os vizinhos ortogonais (NX, NY)
            (NX is X, NY is Y - 1 ; % Cima
             NX is X, NY is Y + 1 ; % Baixo
             NX is X - 1, NY is Y ; % Esquerda
             NX is X + 1, NY is Y), % Direita

            % 2. Garante que não tentamos índices negativos (segurança para o at_index)
            NX >= 0, NY >= 0,

            % 3. Vai buscar a matriz à base de dados
            route(Matrix),

            % 4. Acede à posição usando a tua função recursiva
            at_index(NY, Matrix, Row),
            at_index(NX, Row, (Id, Level)),

            % 5. Filtra a posição inicial e o ID 0
            Id \= 0,

            % 6. Cruza o ID com a lista de nomes e tipos
            pokemon(Id, Name, Types)
        ),
        Rooms).