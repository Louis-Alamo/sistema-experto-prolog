:- use_module(library(lists)).

% Lee el valor de cada pregunta general
valor_g(ID, V) :- respuesta(ID, V).

% Reglas de activación
activar_modulo(ansiedad) :-
    valor_g(g2, G2), valor_g(g7, G7), valor_g(g11, G11),
    Suma is G2 + G7 + G11, Suma >= 6.

activar_modulo(depresion) :-
    valor_g(g1, G1), valor_g(g3, G3), valor_g(g13, G13),
    Suma is G1 + G3 + G13, Suma >= 6.

activar_modulo(estres) :-
    valor_g(g2, G2), valor_g(g4, G4), valor_g(g5, G5),
    Suma is G2 + G4 + G5, Suma >= 6.

activar_modulo(duelo) :-
    valor_g(g12, G12), valor_g(g15, G15),
    Suma is G12 + G15, Suma >= 4.

activar_modulo(autoestima) :-
    valor_g(g14, G14), G14 >= 3.

activar_modulo(tdah) :-
    valor_g(g9, G9), valor_g(g10, G10), valor_g(g11, G11),
    Suma is G9 + G10 + G11, Suma >= 6.

% Lista todos los módulos activos
modulos_activos(Modulos) :-
    findall(M, activar_modulo(M), Modulos).
