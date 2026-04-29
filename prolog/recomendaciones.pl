
mensaje_diagnostico(ansiedad, moderado,
    'Tus respuestas muestran indicios leves de ansiedad. Vale la pena prestarles atencion antes de que crezcan.').

mensaje_diagnostico(ansiedad, alto,
    'Tus respuestas sugieren niveles elevados de ansiedad. Cuando es frecuente e intensa puede afectar tu calidad de vida.').

mensaje_diagnostico(ansiedad, muy_alto,
    'Presentas indicios marcados de ansiedad. Es importante buscar apoyo para trabajar esto.').

% ---

mensaje_diagnostico(depresion, moderado,
    'Tus respuestas muestran algunos indicios de animo bajo. No los ignores, atiendelos a tiempo.').

mensaje_diagnostico(depresion, alto,
    'Tus respuestas indican que podrias estar pasando por un periodo de animo bajo o depresion. No significa debilidad; tiene solucion.').

mensaje_diagnostico(depresion, muy_alto,
    'Tus respuestas muestran indicios marcados de depresion. Buscar apoyo profesional es muy importante en este momento.').

% ---

mensaje_diagnostico(estres, moderado,
    'Tus respuestas muestran un nivel moderado de estres. Conviene atenderlo antes de que escale.').

mensaje_diagnostico(estres, alto,
    'Parece que estas manejando una carga de estres considerable. El estres prolongado afecta la salud fisica y emocional.').

mensaje_diagnostico(estres, muy_alto,
    'Tus respuestas indican una carga de estres muy alta. Es urgente buscar estrategias de manejo o apoyo profesional.').

% ---

mensaje_diagnostico(duelo, moderado,
    'Tus respuestas sugieren que estas procesando una perdida. El duelo es normal, pero merece atencion.').

mensaje_diagnostico(duelo, alto,
    'Parece que atraviesas un proceso de duelo activo que necesita espacio y cuidado.').

mensaje_diagnostico(duelo, muy_alto,
    'Tus respuestas indican un duelo intenso. Acompanar este proceso con un profesional puede ser de gran ayuda.').

% ---

mensaje_diagnostico(autoestima, moderado,
    'Tus respuestas muestran algunos indicios de autoestima baja. Trabajarla puede mejorar muchas areas de tu vida.').

mensaje_diagnostico(autoestima, alto,
    'Tus respuestas muestran indicios claros de autoestima baja. La forma en que te ves influye en casi todo lo que haces.').

mensaje_diagnostico(autoestima, muy_alto,
    'Tus respuestas indican una autoestima muy baja. Es posible trabajarla, pero lo ideal es hacerlo con acompanamiento profesional.').

% ---

mensaje_diagnostico(tdah, moderado,
    'Tus respuestas muestran algunos patrones de atencion e impulsividad. Puede ser util explorarlos.').

mensaje_diagnostico(tdah, alto,
    'Tus respuestas coinciden con varios rasgos asociados al TDAH. Solo un profesional puede confirmarlo.').

mensaje_diagnostico(tdah, muy_alto,
    'Tus respuestas muestran muchos indicadores asociados al TDAH. Una evaluacion profesional es muy recomendable.').


% ------------------------------------------------------------
%  RECOMENDACIONES GENERALES POR CONDICION
%  (se muestran en todos los niveles, salvo "bajo")
% ------------------------------------------------------------

% -- ANSIEDAD --
recomendacion(ansiedad, 'Practica respiracion diafragmatica: inhala 4s, sostén 4s, exhala 6s.').
recomendacion(ansiedad, 'Sal a caminar al menos 20 minutos al dia; el movimiento reduce el cortisol.').
recomendacion(ansiedad, 'Limita el consumo de cafeina y alcohol.').
recomendacion(ansiedad, 'Escribe en un diario lo que te preocupa: sacarlo de la mente al papel lo reduce.').
recomendacion(ansiedad, 'Practica grounding: nombra 5 cosas que ves, 4 que tocas, 3 que escuchas.').
recomendacion(ansiedad, 'Reduce el tiempo en redes sociales, especialmente antes de dormir.').
recomendacion(ansiedad, 'Considera acudir con un psicologo para trabajar tecnicas cognitivo-conductuales.').

% -- DEPRESION --
recomendacion(depresion, 'Establece una rutina diaria sencilla: levantarte, comer y dormir a horas fijas.').
recomendacion(depresion, 'Sal al sol aunque sea 15 minutos al dia; la luz natural regula el estado de animo.').
recomendacion(depresion, 'Haz algo pequeno que antes disfrutaras, aunque no tengas ganas: musica, dibujar, cocinar.').
recomendacion(depresion, 'Habla con alguien de confianza sobre como te sientes.').
recomendacion(depresion, 'Evita el aislamiento; aunque cueste, mantén contacto con personas cercanas.').
recomendacion(depresion, 'Muevete: incluso una caminata corta libera endorfinas.').
recomendacion(depresion, 'Consulta a un psicologo o psiquiatra. No tienes que enfrentar esto solo.').

% -- ESTRES --
recomendacion(estres, 'Aprende a decir no: no puedes con todo, y esta bien reconocerlo.').
recomendacion(estres, 'Haz listas de prioridades: separa lo urgente de lo importante.').
recomendacion(estres, 'Toma descansos activos: levantate cada hora y estira el cuerpo.').
recomendacion(estres, 'Dedica al menos 30 minutos al dia a algo que disfrutes sin que sea una obligacion.').
recomendacion(estres, 'Practica meditacion o mindfulness aunque sea 5 minutos al dia.').
recomendacion(estres, 'Duerme minimo 7 horas: el sueno es clave para gestionar el estres.').
recomendacion(estres, 'Un psicologo puede ayudarte a desarrollar mejores estrategias de manejo del estres.').

% -- DUELO --
recomendacion(duelo, 'Permitete sentir: la tristeza, el enojo y la confusion son parte normal del proceso.').
recomendacion(duelo, 'No te presiones a superarlo rapido; el duelo tiene su propio ritmo.').
recomendacion(duelo, 'Busca un espacio seguro para expresar lo que sientes: escribe, dibuja, habla.').
recomendacion(duelo, 'Honra lo que perdiste a tu manera: un recuerdo, una carta, un ritual propio.').
recomendacion(duelo, 'Rodeate de personas que puedan escucharte sin juzgarte.').
recomendacion(duelo, 'Cuida lo basico: come, duerme y muevete aunque no tengas ganas.').
recomendacion(duelo, 'La terapia de duelo con un psicologo puede acompanar muy bien este proceso.').

% -- AUTOESTIMA --
recomendacion(autoestima, 'Lleva un diario de logros: anota cada dia 3 cosas que hiciste bien.').
recomendacion(autoestima, 'Desafia tus pensamientos negativos: tienes pruebas reales de que son ciertos?').
recomendacion(autoestima, 'Rodeate de personas que te traten bien y te valoren.').
recomendacion(autoestima, 'Aprende algo nuevo: dominar una habilidad incrementa la confianza en uno mismo.').
recomendacion(autoestima, 'Reduce la comparacion con los demas, especialmente en redes sociales.').
recomendacion(autoestima, 'Hablate como lo harias con un amigo que quieres.').
recomendacion(autoestima, 'Un psicologo puede ayudarte a construir una imagen propia mas sana y compasiva.').

% -- TDAH --
recomendacion(tdah, 'Usa listas y recordatorios visuales: post-its, apps, calendarios con alarmas.').
recomendacion(tdah, 'Divide las tareas grandes en pasos pequenos y concretos.').
recomendacion(tdah, 'Trabaja en bloques cortos: 25 min de trabajo, 5 min de descanso (tecnica Pomodoro).').
recomendacion(tdah, 'Silencia notificaciones cuando necesites concentrarte.').
recomendacion(tdah, 'Haz ejercicio con regularidad: tiene efecto positivo comprobado en la concentracion.').
recomendacion(tdah, 'Cuida el sueno y la alimentacion: impactan directamente en la atencion.').
recomendacion(tdah, 'Acude con un psicologo o psiquiatra para una evaluacion formal.').
