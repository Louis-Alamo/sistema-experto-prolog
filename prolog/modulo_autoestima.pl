% -*- coding: utf-8 -*-
:- encoding(utf8).

pregunta_modulo(autoestima, au1, '¿Con qué frecuencia te comparas con los demás y sientes que siempre llevas las de perder?').
pregunta_modulo(autoestima, au2, '¿Con qué frecuencia te cuesta aceptar un cumplido o reconocimiento de otra persona?').
pregunta_modulo(autoestima, au3, '¿Con qué frecuencia evitas intentar algo nuevo por miedo a fracasar o al qué dirán?').
pregunta_modulo(autoestima, au4, '¿Con qué frecuencia sientes que tus opiniones o ideas no valen la pena compartirlas?').
pregunta_modulo(autoestima, au5, '¿Con qué frecuencia te criticas duramente cuando cometes un error?').
pregunta_modulo(autoestima, au6, '¿Con qué frecuencia sientes que necesitas la aprobación de los demás para sentirte bien contigo mismo/a?').
pregunta_modulo(autoestima, au7, '¿Con qué frecuencia sientes vergüenza de quién eres o de cómo te ves?').
pregunta_modulo(autoestima, au8, '¿Con qué frecuencia piensas que no mereces cosas buenas en tu vida?').



puntaje_autoestima(Total) :-
    respuesta(au1, AU1), respuesta(au2, AU2), respuesta(au3, AU3),
    respuesta(au4, AU4), respuesta(au5, AU5), respuesta(au6, AU6),
    respuesta(au7, AU7), respuesta(au8, AU8),
    Total is AU1 + AU2 + AU3 + AU4 + AU5 + AU6 + AU7 + AU8.
