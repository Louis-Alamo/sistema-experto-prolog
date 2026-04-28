
puntaje_duelo(Total) :-
    respuesta(a1, A1), respuesta(a2, A2), respuesta(a3, A3),
    respuesta(a4, A4), respuesta(a5, A5), respuesta(a6, A6),
    respuesta(a7, A7), respuesta(a8, A8),
    Total is A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8.

pregunta_modulo(tdah, a1, '¿Con qué frecuencia comienzas tareas o proyectos y los dejas sin terminar porque perdiste el interés?').
pregunta_modulo(tdah, a2, '¿Con qué frecuencia te olvidas de citas, compromisos o cosas que debías hacer?').
pregunta_modulo(tdah, a3, '¿Con qué frecuencia te resulta muy difícil mantener la atención en algo que no te llama la atención, aunque sea importante?').
pregunta_modulo(tdah, a4, '¿Con qué frecuencia pierdes objetos cotidianos (llaves, celular, documentos)?').
pregunta_modulo(tdah, a5, '¿Con qué frecuencia te distraes con ruidos o cosas que están pasando alrededor cuando intentas concentrarte?').
pregunta_modulo(tdah, a6, '¿Con qué frecuencia sientes una inquietud interna, como si necesitaras estar en movimiento constantemente?').
pregunta_modulo(tdah, a7, '¿Con qué frecuencia actúas o hablas sin pensar primero y luego te arrepientes?').
pregunta_modulo(tdah, a8, '¿Con qué frecuencia tienes dificultad para organizar tus actividades, aunque sabes lo que tienes que hacer?').
pregunta_modulo(tdah, a9, '¿Con qué frecuencia dejas las cosas para el último momento aunque sabes que no es buena idea?').
pregunta_modulo(tdah, a10, '¿Con qué frecuencia en situaciones sociales o de trabajo interrumpes a otros o terminas sus frases?').
