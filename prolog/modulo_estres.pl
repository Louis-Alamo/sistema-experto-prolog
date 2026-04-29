% -*- coding: utf-8 -*-
:- encoding(utf8).

pregunta_modulo(estres, e1, '¿Con qué frecuencia sientes que tienes más responsabilidades de las que puedes manejar?').
pregunta_modulo(estres, e2, '¿Con qué frecuencia sientes que el tiempo no te alcanza para todo lo que tienes que hacer?').
pregunta_modulo(estres, e3, '¿Con qué frecuencia llegas al final del día sintiéndote completamente agotado/a?').
pregunta_modulo(estres, e4, '¿Con qué frecuencia sientes que estás "al límite" y que cualquier cosa pequeña te desespera?').
pregunta_modulo(estres, e5, '¿Con qué frecuencia el trabajo, la escuela o tus obligaciones te quitan tiempo de descanso?').
pregunta_modulo(estres, e6, '¿Con qué frecuencia sientes que no puedes "desconectarte" aunque quieras?').
pregunta_modulo(estres, e7, '¿Con qué frecuencia has tenido conflictos con personas cercanas por estar estresado/a?').
pregunta_modulo(estres, e8, '¿Con qué frecuencia recurres a cosas como comer en exceso, redes sociales o pantallas para "escapar" del estrés?').


puntaje_estres(Total) :-
    respuesta(e1, E1), respuesta(e2, E2), respuesta(e3, E3),
    respuesta(e4, E4), respuesta(e5, E5), respuesta(e6, E6),
    respuesta(e7, E7), respuesta(e8, E8),
    Total is E1 + E2 + E3 + E4 + E5 + E6 + E7 + E8.
