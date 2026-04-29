% -*- coding: utf-8 -*-
:- encoding(utf8).

% Calcula el puntaje total de ansiedad
% Requiere que Python haya asertado: respuesta(a1, V), respuesta(a2, V)... etc.

puntaje_ansiedad(Total) :-
    respuesta(a1, A1), respuesta(a2, A2), respuesta(a3, A3),
    respuesta(a4, A4), respuesta(a5, A5), respuesta(a6, A6),
    respuesta(a7, A7), respuesta(a8, A8),
    Total is A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8.

% Definicion de las preguntas (Python las lee para mostrarlas)
pregunta_modulo(ansiedad, a1, 'Sientes peligro o amenaza sin que haya causa real?').
pregunta_modulo(ansiedad, a2, 'Tienes episodios de corazon acelerado o falta de aire?').
pregunta_modulo(ansiedad, a3, 'Evitas situaciones o lugares porque te generan miedo?').
pregunta_modulo(ansiedad, a4, 'Tu preocupacion es tan intensa que no puedes hacer nada?').
pregunta_modulo(ansiedad, a5, 'Te pones en el peor escenario posible antes de que pase?').
pregunta_modulo(ansiedad, a6, 'Sientes que algo malo va a pasar sin saber que?').
pregunta_modulo(ansiedad, a7, 'Tienes pensamientos repetitivos que no puedes detener?').
pregunta_modulo(ansiedad, a8, 'Necesitas que todo salga perfectamente o te angustias?').
