% -*- coding: utf-8 -*-
:- encoding(utf8).

puntaje_duelo(Total) :-
    respuesta(du1, A1), respuesta(du2, A2), respuesta(du3, A3),
    respuesta(du4, A4), respuesta(du5, A5), respuesta(du6, A6),
    respuesta(du7, A7), respuesta(du8, A8),
    Total is A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8.

pregunta_modulo(duelo, du1, "¿Con qué frecuencia piensas en la persona, relación o situación que perdiste?").
pregunta_modulo(duelo, du2, "¿Con qué frecuencia sientes que esa pérdida fue injusta o que no lo mereces?").
pregunta_modulo(duelo, du3, "¿Con qué frecuencia sientes enojo, culpa o tristeza profunda cuando piensas en esa pérdida?").
pregunta_modulo(duelo, du4, '¿Con qué frecuencia evitas hablar o pensar en lo que perdiste porque te genera demasiado dolor?').
pregunta_modulo(duelo, du5, '¿Con qué frecuencia sientes que la vida ya no tiene el mismo sentido desde esa pérdida?').
pregunta_modulo(duelo, du6, '¿Con qué frecuencia tienes dificultad para aceptar que esa pérdida es real o definitiva?').
pregunta_modulo(duelo, du7, '¿Con qué frecuencia sientes que no puedes seguir adelante o que estás atascado/a en ese momento?').
pregunta_modulo(duelo, du8, '¿Con qué frecuencia sientes que necesitas hablar de esa pérdida pero no sabes con quién?').
