# -*- coding: utf-8 -*-
"""
prolog_bridge.py
Capa de comunicación entre Python y Prolog usando pyswip.
Incluye un PrologBridgeMock para pruebas de UI sin Prolog instalado.
"""

import os
import sys


if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')


# ══════════════════════════════════════════════════════════════════════════════
# Bridge real — requiere pyswip y SWI-Prolog instalados
# ══════════════════════════════════════════════════════════════════════════════

class PrologBridge:
    """Puente de comunicación entre Python y Prolog usando pyswip."""

    def __init__(self):
        from pyswip import Prolog  # Import diferido para no romper al importar
        self.prolog = Prolog()
        ruta = os.path.join(os.path.dirname(__file__), '..', 'prolog', 'main.pl')
        ruta = os.path.abspath(ruta)
        self.prolog.consult(ruta)

    def _decodificar(self, valor):
        """Decodifica valores desde Prolog a strings UTF-8."""
        if isinstance(valor, bytes):
            return valor.decode('utf-8')
        return str(valor)

    def guardar_respuesta(self, pregunta_id: str, valor: int):
        """Inserta una respuesta en la base de conocimiento de Prolog."""
        self.prolog.retractall(f"respuesta({pregunta_id}, _)")
        self.prolog.assertz(f"respuesta({pregunta_id}, {valor})")

    def obtener_modulos_activos(self) -> list[str]:
        """Devuelve la lista de módulos que Prolog activa."""
        resultado = list(self.prolog.query("modulos_activos(M)"))
        if resultado:
            return [self._decodificar(m) for m in resultado[0]['M']]
        return []

    def obtener_preguntas_modulo(self, modulo: str) -> list[dict]:
        """Obtiene las preguntas de un módulo desde Prolog."""
        query = f"pregunta_modulo({modulo}, ID, Texto)"
        resultado = list(self.prolog.query(query))
        return [{'id': self._decodificar(r['ID']), 'texto': self._decodificar(r['Texto'])} for r in resultado]

    def obtener_diagnosticos(self) -> list[dict]:
        """Obtiene todos los diagnósticos activos."""
        query = "diagnostico_completo(Condicion, Puntaje, Nivel)"
        resultado = list(self.prolog.query(query))
        return [
            {
                'condicion': self._decodificar(r['Condicion']),
                'puntaje':   int(r['Puntaje']),
                'nivel':     self._decodificar(r['Nivel']),
            }
            for r in resultado
        ]

    def obtener_recomendaciones(self, condicion: str) -> list[str]:
        """Obtiene las recomendaciones de una condición."""
        query = f"recomendacion({condicion}, Texto)"
        resultado = list(self.prolog.query(query))
        return [self._decodificar(r['Texto']) for r in resultado]

    def alerta_depresion_grave(self) -> bool:
        """Detecta si D3 fue respondida con a_menudo (3) o siempre (4)."""
        resultado = list(self.prolog.query("respuesta(d3, V), V >= 3"))
        return len(resultado) > 0


# ══════════════════════════════════════════════════════════════════════════════
# Mock — para pruebas de UI sin Prolog
# ══════════════════════════════════════════════════════════════════════════════

class PrologBridgeMock:
    """
    Versión simulada del bridge para probar la interfaz sin Prolog.
    Activa los módulos ansiedad, duelo y tdah por defecto.
    """

    def __init__(self):
        self._respuestas: dict[str, int] = {}

    def guardar_respuesta(self, pregunta_id: str, valor: int):
        self._respuestas[pregunta_id] = valor

    def obtener_modulos_activos(self) -> list[str]:
        return ["ansiedad", "duelo", "tdah"]

    def obtener_preguntas_modulo(self, modulo: str) -> list[dict]:
        preguntas_mock = {
            "ansiedad": [
                {"id": "a1", "texto": "¿Sientes peligro o amenaza sin que haya causa real?"},
                {"id": "a2", "texto": "¿Tienes episodios de corazón acelerado o falta de aire?"},
                {"id": "a3", "texto": "¿Evitas situaciones o lugares porque te generan miedo?"},
                {"id": "a4", "texto": "¿Tu preocupación es tan intensa que no puedes hacer nada?"},
                {"id": "a5", "texto": "¿Te pones en el peor escenario posible antes de que pase?"},
                {"id": "a6", "texto": "¿Sientes que algo malo va a pasar sin saber qué?"},
                {"id": "a7", "texto": "¿Tienes pensamientos repetitivos que no puedes detener?"},
                {"id": "a8", "texto": "¿Necesitas que todo salga perfectamente o te angustias?"},
            ],
            "duelo": [
                {"id": "du1", "texto": "¿Con qué frecuencia piensas en la persona o situación que perdiste?"},
                {"id": "du2", "texto": "¿Con qué frecuencia sientes que esa pérdida fue injusta?"},
                {"id": "du3", "texto": "¿Con qué frecuencia sientes enojo, culpa o tristeza profunda?"},
                {"id": "du4", "texto": "¿Con qué frecuencia evitas hablar de lo que perdiste?"},
                {"id": "du5", "texto": "¿Con qué frecuencia sientes que la vida perdió el mismo sentido?"},
                {"id": "du6", "texto": "¿Con qué frecuencia tienes dificultad para aceptar esa pérdida?"},
                {"id": "du7", "texto": "¿Con qué frecuencia sientes que no puedes seguir adelante?"},
                {"id": "du8", "texto": "¿Con qué frecuencia necesitas hablar de esa pérdida pero no sabes con quién?"},
            ],
            "tdah": [
                {"id": "t1",  "texto": "¿Con qué frecuencia dejas tareas sin terminar por perder el interés?"},
                {"id": "t2",  "texto": "¿Con qué frecuencia te olvidas de citas o compromisos?"},
                {"id": "t3",  "texto": "¿Con qué frecuencia te cuesta mantener la atención en algo importante?"},
                {"id": "t4",  "texto": "¿Con qué frecuencia pierdes objetos cotidianos (llaves, celular)?"},
                {"id": "t5",  "texto": "¿Con qué frecuencia te distraes con ruidos del entorno?"},
                {"id": "t6",  "texto": "¿Con qué frecuencia sientes inquietud interna constante?"},
                {"id": "t7",  "texto": "¿Con qué frecuencia actúas sin pensar y luego te arrepientes?"},
                {"id": "t8",  "texto": "¿Con qué frecuencia tienes dificultad para organizar tus actividades?"},
                {"id": "t9",  "texto": "¿Con qué frecuencia dejas todo para el último momento?"},
                {"id": "t10", "texto": "¿Con qué frecuencia interrumpes a otros o terminas sus frases?"},
            ],
        }
        return preguntas_mock.get(modulo, [])

    def obtener_diagnosticos(self) -> list[dict]:
        def nivel(pts):
            if pts >= 25: return "muy_alto"
            if pts >= 17: return "alto"
            if pts >= 9:  return "moderado"
            return "bajo"

        ansiedad_pts = sum(self._respuestas.get(f"a{i}", 2) for i in range(1, 9))
        duelo_pts    = sum(self._respuestas.get(f"du{i}", 1) for i in range(1, 9))
        tdah_pts     = sum(self._respuestas.get(f"t{i}", 2) for i in range(1, 11))

        return [
            {"condicion": "ansiedad", "puntaje": ansiedad_pts, "nivel": nivel(ansiedad_pts)},
            {"condicion": "duelo",    "puntaje": duelo_pts,    "nivel": nivel(duelo_pts)},
            {"condicion": "tdah",     "puntaje": tdah_pts,     "nivel": nivel(tdah_pts)},
        ]

    def obtener_recomendaciones(self, condicion: str) -> list[str]:
        recs = {
            "ansiedad": [
                "Practica respiración diafragmática: inhala 4s, sostén 4s, exhala 6s.",
                "Limita el consumo de cafeína y alcohol.",
                "Practica grounding: nombra 5 cosas que ves, 4 que tocas, 3 que escuchas.",
                "Considera acudir con un psicólogo para técnicas cognitivo-conductuales.",
            ],
            "duelo": [
                "Permítete sentir: la tristeza y el enojo son parte normal del proceso.",
                "No te presiones a superarlo rápido; el duelo tiene su propio ritmo.",
                "Busca un espacio seguro para expresar lo que sientes.",
                "La terapia de duelo con un psicólogo puede acompañar muy bien este proceso.",
            ],
            "tdah": [
                "Usa listas y recordatorios visuales: post-its, apps, calendarios.",
                "Divide las tareas grandes en pasos pequeños y concretos.",
                "Trabaja en bloques: 25 min de trabajo, 5 min de descanso (Pomodoro).",
                "Acude con un psicólogo o psiquiatra para una evaluación formal.",
            ],
        }
        return recs.get(condicion, ["Mantén hábitos saludables y busca apoyo profesional."])

    def alerta_depresion_grave(self) -> bool:
        return self._respuestas.get("d3", 0) >= 3

