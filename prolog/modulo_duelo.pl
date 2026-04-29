
puntaje_duelo(Total) :-
    respuesta(a1, A1), respuesta(a2, A2), respuesta(a3, A3),
    respuesta(a4, A4), respuesta(a5, A5), respuesta(a6, A6),
    respuesta(a7, A7), respuesta(a8, A8),
    Total is A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8.

pregunta_modulo(duelo, a1, '¿Con qué frecuencia piensas en la persona, relación o situación que perdiste?').
pregunta_modulo(duelo, a2, '¿Con qué frecuencia sientes que esa pérdida fue injusta o que no lo mereces?').
pregunta_modulo(duelo, a3, '¿Con qué frecuencia sientes enojo, culpa o tristeza profunda cuando piensas en esa pérdida?').
pregunta_modulo(duelo, a4, '¿Con qué frecuencia evitas hablar o pensar en lo que perdiste porque te genera demasiado dolor?').
pregunta_modulo(duelo, a5, '¿Con qué frecuencia sientes que la vida ya no tiene el mismo sentido desde esa pérdida?').
pregunta_modulo(duelo, a6, '¿Con qué frecuencia tienes dificultad para aceptar que esa pérdida es real o definitiva?').
pregunta_modulo(duelo, a7, '¿Con qué frecuencia sientes que no puedes seguir adelante o que estás atascado/a en ese momento?').
pregunta_modulo(duelo, a8, '¿Con qué frecuencia sientes que necesitas hablar de esa pérdida pero no sabes con quién?').
