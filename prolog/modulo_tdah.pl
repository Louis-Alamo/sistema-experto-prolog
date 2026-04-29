% -*- coding: utf-8 -*-
:- encoding(utf8).

puntaje_tdah(Total) :-
    respuesta(t1, V1), respuesta(t2, V2), respuesta(t3, V3),
    respuesta(t4, V4), respuesta(t5, V5), respuesta(t6, V6),
    respuesta(t7, V7), respuesta(t8, V8), respuesta(t9, V9),
    respuesta(t10, V10),
    Total is V1 + V2 + V3 + V4 + V5 + V6 + V7 + V8 + V9 + V10.

pregunta_modulo(tdah, t1,  '¿Con qué frecuencia comienzas tareas o proyectos y los dejas sin terminar porque perdiste el interés?').
pregunta_modulo(tdah, t2,  '¿Con qué frecuencia te olvidas de citas, compromisos o cosas que debías hacer?').
pregunta_modulo(tdah, t3,  '¿Con qué frecuencia te resulta muy difícil mantener la atención en algo que no te llama la atención, aunque sea importante?').
pregunta_modulo(tdah, t4,  '¿Con qué frecuencia pierdes objetos cotidianos (llaves, celular, documentos)?').
pregunta_modulo(tdah, t5,  '¿Con qué frecuencia te distraes con ruidos o cosas que están pasando alrededor cuando intentas concentrarte?').
pregunta_modulo(tdah, t6,  '¿Con qué frecuencia sientes una inquietud interna, como si necesitaras estar en movimiento constantemente?').
pregunta_modulo(tdah, t7,  '¿Con qué frecuencia actúas o hablas sin pensar primero y luego te arrepientes?').
pregunta_modulo(tdah, t8,  '¿Con qué frecuencia tienes dificultad para organizar tus actividades, aunque sabes lo que tienes que hacer?').
pregunta_modulo(tdah, t9,  '¿Con qué frecuencia dejas las cosas para el último momento aunque sabes que no es buena idea?').
pregunta_modulo(tdah, t10, '¿Con qué frecuencia en situaciones sociales o de trabajo interrumpes a otros o terminas sus frases?').
