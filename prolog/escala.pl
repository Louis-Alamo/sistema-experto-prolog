% Convierte respuesta a número
escala_valor(nunca,      0).
escala_valor(casi_nunca, 1).
escala_valor(a_veces,    2).
escala_valor(a_menudo,   3).
escala_valor(siempre,    4).

% Obtiene el valor numérico de una respuesta guardada
valor_respuesta(Pregunta, Valor) :-
    respuesta(Pregunta, Valor).  % respuesta/2 lo aserta Python
