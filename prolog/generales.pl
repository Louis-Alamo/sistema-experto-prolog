% -*- coding: utf-8 -*-
:- encoding(utf8).

% Preguntas generales

pregunta_general(g1, '¿Con qué frecuencia te sientes triste o con el ánimo muy bajo?').
pregunta_general(g2, '¿Con qué frecuencia sientes que te preocupas demasiado por cosas del día a día?').
pregunta_general(g3, '¿Con qué frecuencia sientes que no tienes energía para hacer tus actividades?').
pregunta_general(g4, '¿Con qué frecuencia tu estado de ánimo afecta tu vida diaria?').
pregunta_general(g5, '¿Con qué frecuencia te sientes irritable o de mal humor sin una razón clara?').
pregunta_general(g6, '¿Con qué frecuencia tienes dificultad para dormir (tardar en conciliar el sueño, despertarse de madrugada)?').
pregunta_general(g7, '¿Con qué frecuencia sientes tensión muscular, dolor de cabeza o malestar físico sin causa médica?').
pregunta_general(g8, '¿Con qué frecuencia sientes que tu apetito ha cambiado (comes mucho más o menos de lo normal)?').
pregunta_general(g9, '¿Con qué frecuencia te cuesta concentrarte en lo que estás haciendo?').
pregunta_general(g10, '¿Con qué frecuencia dejas tareas o compromisos sin terminar?').
pregunta_general(g11, '¿Con qué frecuencia sientes que tu mente salta de pensamiento a otro sin poder detenerte?').
pregunta_general(g12, '¿Con qué frecuencia te has alejado de personas que antes eran importantes para ti?').
pregunta_general(g13, '¿Con qué frecuencia sientes que has perdido interés en actividades que antes disfrutabas?').
pregunta_general(g14, '¿Con qué frecuencia sientes que no vales lo suficiente o que los demás son mejores que tú?').
pregunta_general(g15, '¿Con qué frecuencia has experimentado alguna pérdida importante (persona, relación, trabajo) recientemente?').



% Obtener TODAS las 15 preguntas generales en una sola consulta
todas_preguntas_generales(Preguntas) :-
    findall({'ID': ID, 'Texto': Texto}, pregunta_general(ID, Texto), Preguntas).
