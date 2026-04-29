
pregunta_modulo(depresion, d1, '¿Con qué frecuencia sientes que nada te da alegría, ni siquiera cosas que antes te gustaban?').
pregunta_modulo(depresion, d2, '¿Con qué frecuencia te sientes vacío/a o sin esperanza sobre el futuro?').
pregunta_modulo(depresion, d3, '¿Con qué frecuencia tienes pensamientos como "sería mejor no estar aquí" o de hacerte daño?').
pregunta_modulo(depresion, d4, '¿Con qué frecuencia sientes que todo es un esfuerzo enorme, incluso levantarte de la cama?').
pregunta_modulo(depresion, d5, '¿Con qué frecuencia lloras sin saber bien por qué?').
pregunta_modulo(depresion, d6, '¿Con qué frecuencia sientes que eres una carga para las personas que te rodean?').
pregunta_modulo(depresion, d7, '¿Con qué frecuencia has perdido el deseo o la motivación de planear cosas para el futuro?').
pregunta_modulo(depresion, d8, '¿Con qué frecuencia te has aislado de amigos o familia porque no tienes ganas de socializar?').


puntaje_depresion(Total) :-
    respuesta(d1, D1), respuesta(d2, D2), respuesta(d3, D3),
    respuesta(d4, D4), respuesta(d5, D5), respuesta(d6, D6),
    respuesta(d7, D7), respuesta(d8, D8),
    Total is D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8.



alerta_depresion_grave :- respuesta(d3, V), V >= 3.
