:-ensure_loaded("pokemon_list.pl").
:-ensure_loaded("pokemon_info_attacks.pl").
:-ensure_loaded("pokemon_route.pl").

player_starts(0,0).
next_rooms(X,Y,Rooms) :-
                                    % 1. Encontra todos os conjuntos de dados que satisfaçam as condições abaixo
findall([Id, Name, Level, NX, NY, Types], %------
(
                                    % 2. Define os vizinhos ortogonais (NX, NY)
(NX is X, NY is Y - 1 ;                                     % Cima
NX is X, NY is Y + 1 ;                                      % Baixo
NX is X - 1, NY is Y ;                                      % Esquerda
NX is X + 1, NY is Y),                                      % Direita
                                    % 3. Vai buscar a matriz à base de dados (ficheiro pokemon_route.pl)
route(Matrix),                             %---------
                                    % 4. Tenta aceder à posição. Se NX ou NY estiverem fora da matriz, o nth0 falha
nth0(NY, Matrix, Row),                 % Procura a linha Y
nth0(NX, Row, (Id, Level)),            % Procura o par (Id, Level) na coluna X
                                    % 5. Filtra a posição (0,0) que é o início (não é um pokémon combatível)
Id \= 0,
                                    % 6. Cruza o ID com a lista de nomes e tipos (ficheiro pokemon_list.pl)
pokemon(Id, Name, Types)
),
Rooms).