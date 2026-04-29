% clasificacion de nivel

nivel_diagnostico(_, P, muy_alto) :- P >= 25, !.
nivel_diagnostico(_, P, alto) :- P >= 17, !.
nivel_diagnostico(_, P, moderado) :- P >= 9, !.
nivel_diagnostico(_, _, bajo).

% Puntuajes por modulo

puntaje_modulo(ansiedad, P) :- puntaje_ansiedad(P).
puntaje_modulo(depresion, P) :- puntaje_depresion(P).
puntaje_modulo(estres, P) :- puntaje_estres(P).
puntaje_modulo(duelo, P) :- puntaje_duelo(P).
puntaje_modulo(autoestima, P) :- puntaje_autoestima(P).
puntaje_modulo(tdah, P) :- puntaje_tdah(P).



diagnostico_completo(Condicion, Puntaje, Nivel) :-
    activar_modulo(Condicion),
    puntaje_modulo(Condicion, Puntaje),
    nivel_diagnostico(Condicion, Puntaje, Nivel).
