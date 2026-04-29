
---

## La Idea Central

Python y Prolog se dividen el trabajo así:

| Capa | Tecnología | Responsabilidad |
|---|---|---|
| **Interfaz** | Python (tkinter / Flask) | Mostrar preguntas, animaciones, resultados bonitos |
| **Puente** | `pyswip` (librería Python) | Conectar ambos mundos |
| **Motor de Inferencia** | Prolog (SWI-Prolog) | Toda la lógica: activar módulos, calcular puntajes, dar diagnóstico |

> **Flujo resumido:** Python muestra pregunta → usuario responde → Python *aserta* la respuesta en Prolog → al final Python *consulta* a Prolog el diagnóstico → Python muestra el resultado bonito.

---

## ¿Qué es `pyswip` y cómo funciona?

`pyswip` es una librería Python que habla directamente con SWI-Prolog desde código Python. Con ella puedes:

```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("main.pl")         # Carga un archivo .pl

prolog.assertz("respuesta(g1, 3)")  # Inserta un hecho en Prolog

list(prolog.query("modulos_activos(X)"))  # Hace una consulta y trae resultados
```

**Instalación:**
```bash
pip install pyswip
# También necesitas tener SWI-Prolog instalado en el sistema
```

---

## Estructura de Archivos

```
sistema_experto/
│
├── prolog/                        ← Todo el motor de inferencia
│   ├── main.pl                    ← Carga todos los demás
│   ├── escala.pl                  ← Conversión respuesta → número
│   ├── activacion.pl              ← Reglas para saber qué módulos activar
│   ├── diagnostico.pl             ← nivel_diagnostico/2 y resultados
│   ├── recomendaciones.pl         ← Hechos: recomendacion(condicion, texto)
│   │
│   ├── modulo_ansiedad.pl         ← Preguntas A1-A8 y puntaje
│   ├── modulo_depresion.pl        ← Preguntas D1-D8 y puntaje
│   ├── modulo_estres.pl           ← Preguntas E1-E8 y puntaje
│   ├── modulo_duelo.pl            ← Preguntas Du1-Du8 y puntaje
│   ├── modulo_autoestima.pl       ← Preguntas Au1-Au8 y puntaje
│   └── modulo_tdah.pl             ← Preguntas T1-T10 y puntaje
│
└── python/
    ├── main.py                    ← Punto de entrada, arranca la app
    ├── prolog_bridge.py           ← Toda la comunicación con Prolog
    └── ui/
        ├── pantalla_bienvenida.py ← Primera pantalla
        ├── pantalla_preguntas.py  ← Muestra preguntas una por una
        └── pantalla_resultados.py ← Muestra diagnósticos y recomendaciones
```

> **¿Por qué un archivo por módulo?** Facilita editar, depurar y ampliar. Si quieres agregar una pregunta a TDAH, solo tocas `modulo_tdah.pl` sin romper nada más.

---

## Cómo se Comunican: El Truco del `assertz`

El puente entre Python y Prolog funciona así:

```
Python recoge respuesta del usuario
        ↓
Python llama: prolog.assertz("respuesta(g1, 3)")
        ↓
Ahora en Prolog existe el hecho: respuesta(g1, 3).
        ↓
Las reglas Prolog leen ese hecho para calcular todo
        ↓
Python consulta: prolog.query("diagnostico(ansiedad, Nivel, Puntaje)")
        ↓
Python recibe: [{'Nivel': 'alto', 'Puntaje': 22}]
        ↓
Python muestra el resultado bonito
```

---

## Código: `prolog/escala.pl`

```prolog
% Convierte respuesta a número
escala_valor(nunca,      0).
escala_valor(casi_nunca, 1).
escala_valor(a_veces,    2).
escala_valor(a_menudo,   3).
escala_valor(siempre,    4).

% Obtiene el valor numérico de una respuesta guardada
valor_respuesta(Pregunta, Valor) :-
    respuesta(Pregunta, Valor).  % respuesta/2 lo aserta Python
```

> **Nota clave:** Prolog no pregunta nada. Python le dice "el usuario respondió `a_veces` a `g1`" insertando `respuesta(g1, 2)`. Prolog solo *consulta* esos hechos.

---

## Código: `prolog/activacion.pl`

```prolog
:- use_module(library(lists)).

% Lee el valor de cada pregunta general
valor_g(ID, V) :- respuesta(ID, V).

% Reglas de activación
activar_modulo(ansiedad) :-
    valor_g(g2, G2), valor_g(g7, G7), valor_g(g11, G11),
    Suma is G2 + G7 + G11, Suma >= 6.

activar_modulo(depresion) :-
    valor_g(g1, G1), valor_g(g3, G3), valor_g(g13, G13),
    Suma is G1 + G3 + G13, Suma >= 6.

activar_modulo(estres) :-
    valor_g(g2, G2), valor_g(g4, G4), valor_g(g5, G5),
    Suma is G2 + G4 + G5, Suma >= 6.

activar_modulo(duelo) :-
    valor_g(g12, G12), valor_g(g15, G15),
    Suma is G12 + G15, Suma >= 4.

activar_modulo(autoestima) :-
    valor_g(g14, G14), G14 >= 3.

activar_modulo(tdah) :-
    valor_g(g9, G9), valor_g(g10, G10), valor_g(g11, G11),
    Suma is G9 + G10 + G11, Suma >= 6.

% Lista todos los módulos activos
modulos_activos(Modulos) :-
    findall(M, activar_modulo(M), Modulos).
```

---

## Código: `prolog/modulo_ansiedad.pl`

```prolog
% Calcula el puntaje total de ansiedad
% Requiere que Python haya asertado: respuesta(a1, V), respuesta(a2, V)... etc.

puntaje_ansiedad(Total) :-
    respuesta(a1, A1), respuesta(a2, A2), respuesta(a3, A3),
    respuesta(a4, A4), respuesta(a5, A5), respuesta(a6, A6),
    respuesta(a7, A7), respuesta(a8, A8),
    Total is A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8.

% Definicion de las preguntas (Python las lee para mostrarlas)
pregunta_modulo(ansiedad, a1, 'Sientes peligro o amenaza sin que haya causa real?').
pregunta_modulo(ansiedad, a2, 'Tienes episodios de corazon acelerado o falta de aire?').
pregunta_modulo(ansiedad, a3, 'Evitas situaciones o lugares porque te generan miedo?').
pregunta_modulo(ansiedad, a4, 'Tu preocupacion es tan intensa que no puedes hacer nada?').
pregunta_modulo(ansiedad, a5, 'Te pones en el peor escenario posible antes de que pase?').
pregunta_modulo(ansiedad, a6, 'Sientes que algo malo va a pasar sin saber que?').
pregunta_modulo(ansiedad, a7, 'Tienes pensamientos repetitivos que no puedes detener?').
pregunta_modulo(ansiedad, a8, 'Necesitas que todo salga perfectamente o te angustias?').
```

> **¡Importante!** Las preguntas las *almacena* Prolog pero las *muestra* Python. Python consulta `pregunta_modulo(ansiedad, ID, Texto)` para saber qué mostrar.

---

## Código: `prolog/diagnostico.pl`

```prolog
nivel_diagnostico(_, P, muy_alto) :- P >= 25, !.
nivel_diagnostico(_, P, alto)     :- P >= 17, !.
nivel_diagnostico(_, P, moderado) :- P >= 9,  !.
nivel_diagnostico(_, _, bajo).

% Calcula puntaje según condición
puntaje_modulo(ansiedad,  P) :- puntaje_ansiedad(P).
puntaje_modulo(depresion, P) :- puntaje_depresion(P).
puntaje_modulo(estres,    P) :- puntaje_estres(P).
puntaje_modulo(duelo,     P) :- puntaje_duelo(P).
puntaje_modulo(autoestima,P) :- puntaje_autoestima(P).
puntaje_modulo(tdah,      P) :- puntaje_tdah(P).

% Predicado completo: condicion + puntaje + nivel
diagnostico_completo(Condicion, Puntaje, Nivel) :-
    activar_modulo(Condicion),
    puntaje_modulo(Condicion, Puntaje),
    nivel_diagnostico(Condicion, Puntaje, Nivel).
```

---

## Código: `prolog/main.pl`

```prolog
% Carga todos los archivos en orden
:- consult('escala.pl').
:- consult('activacion.pl').
:- consult('modulo_ansiedad.pl').
:- consult('modulo_depresion.pl').
:- consult('modulo_estres.pl').
:- consult('modulo_duelo.pl').
:- consult('modulo_autoestima.pl').
:- consult('modulo_tdah.pl').
:- consult('diagnostico.pl').
:- consult('recomendaciones.pl').

% Las respuestas son dinámicas (Python las inserta en tiempo de ejecución)
:- dynamic respuesta/2.
```

> **`:- dynamic respuesta/2`** le dice a Prolog que `respuesta/2` se agregará en tiempo de ejecución (desde Python), no está definida en el archivo.

---

## Código: `python/prolog_bridge.py`

```python
from pyswip import Prolog
import os

class PrologBridge:
    """Puente de comunicación entre Python y Prolog."""

    def __init__(self):
        self.prolog = Prolog()
        # Ruta al main.pl
        ruta = os.path.join(os.path.dirname(__file__), '..', 'prolog', 'main.pl')
        self.prolog.consult(ruta)

    def guardar_respuesta(self, pregunta_id: str, valor: int):
        """Inserta una respuesta en la base de conocimiento de Prolog."""
        # Elimina respuesta anterior si existe (para reintento)
        self.prolog.retractall(f"respuesta({pregunta_id}, _)")
        self.prolog.assertz(f"respuesta({pregunta_id}, {valor})")

    def obtener_modulos_activos(self) -> list[str]:
        """Pregunta a Prolog qué módulos se activaron."""
        resultado = list(self.prolog.query("modulos_activos(M)"))
        if resultado:
            return resultado[0]['M']  # Lista de átomos Prolog
        return []

    def obtener_preguntas_modulo(self, modulo: str) -> list[dict]:
        """Obtiene las preguntas de un módulo desde Prolog."""
        query = f"pregunta_modulo({modulo}, ID, Texto)"
        resultado = list(self.prolog.query(query))
        return [{'id': str(r['ID']), 'texto': str(r['Texto'])} for r in resultado]

    def obtener_diagnosticos(self) -> list[dict]:
        """Obtiene todos los diagnósticos activos."""
        query = "diagnostico_completo(Condicion, Puntaje, Nivel)"
        resultado = list(self.prolog.query(query))
        return [
            {
                'condicion': str(r['Condicion']),
                'puntaje':   int(r['Puntaje']),
                'nivel':     str(r['Nivel'])
            }
            for r in resultado
        ]

    def obtener_recomendaciones(self, condicion: str) -> list[str]:
        """Obtiene recomendaciones de una condición."""
        query = f"recomendacion({condicion}, Texto)"
        resultado = list(self.prolog.query(query))
        return [str(r['Texto']) for r in resultado]

    def alerta_depresion_grave(self) -> bool:
        """Detecta si D3 fue respondida con a_menudo o siempre."""
        resultado = list(self.prolog.query("respuesta(d3, V), V >= 3"))
        return len(resultado) > 0
```

---

## Código: `python/main.py` — Flujo Principal

```python
from prolog_bridge import PrologBridge
from ui.pantalla_bienvenida import mostrar_bienvenida
from ui.pantalla_preguntas import PantallaPreguntas
from ui.pantalla_resultados import PantallaResultados

# Preguntas generales definidas en Python (o podrías leerlas desde Prolog también)
PREGUNTAS_GENERALES = [
    ('g1',  '¿Con qué frecuencia te sientes triste o con el ánimo muy bajo?'),
    ('g2',  '¿Con qué frecuencia sientes que te preocupas demasiado?'),
    ('g3',  '¿Con qué frecuencia sientes que no tienes energía?'),
    ('g4',  '¿Con qué frecuencia tu estado de ánimo afecta tu vida diaria?'),
    ('g5',  '¿Con qué frecuencia te sientes irritable sin razón clara?'),
    ('g6',  '¿Con qué frecuencia tienes dificultad para dormir?'),
    ('g7',  '¿Con qué frecuencia sientes tensión muscular o dolor de cabeza?'),
    ('g8',  '¿Con qué frecuencia ha cambiado tu apetito?'),
    ('g9',  '¿Con qué frecuencia te cuesta concentrarte?'),
    ('g10', '¿Con qué frecuencia dejas tareas sin terminar?'),
    ('g11', '¿Con qué frecuencia tu mente salta de pensamiento en pensamiento?'),
    ('g12', '¿Con qué frecuencia te has alejado de personas cercanas?'),
    ('g13', '¿Con qué frecuencia perdiste interés en actividades que antes disfrutabas?'),
    ('g14', '¿Con qué frecuencia sientes que no vales lo suficiente?'),
    ('g15', '¿Con qué frecuencia has tenido una pérdida importante recientemente?'),
]

ESCALA = ['Nunca', 'Casi nunca', 'A veces', 'A menudo', 'Siempre']

def main():
    bridge = PrologBridge()
    ui = PantallaPreguntas(ESCALA)

    # 1. Bienvenida
    mostrar_bienvenida()

    # 2. FASE 1 — Preguntas generales
    for id_pregunta, texto in PREGUNTAS_GENERALES:
        valor = ui.mostrar_pregunta(id_pregunta, texto)  # Devuelve 0-4
        bridge.guardar_respuesta(id_pregunta, valor)

    # 3. Preguntar a Prolog qué módulos activar
    modulos = bridge.obtener_modulos_activos()

    if not modulos:
        ui.mostrar_mensaje("¡Sin indicios significativos! Sigue cuidándote.")
        return

    # 4. FASE 2 — Preguntas específicas por módulo activo
    for modulo in modulos:
        preguntas = bridge.obtener_preguntas_modulo(modulo)
        ui.mostrar_encabezado_modulo(modulo)

        for pregunta in preguntas:
            valor = ui.mostrar_pregunta(pregunta['id'], pregunta['texto'])
            bridge.guardar_respuesta(pregunta['id'], valor)

            # Alerta especial para D3 (depresión grave)
            if pregunta['id'] == 'd3' and bridge.alerta_depresion_grave():
                ui.mostrar_alerta_crisis()

    # 5. Pedir diagnósticos a Prolog
    diagnosticos = bridge.obtener_diagnosticos()

    # 6. Mostrar resultados bonitos en Python
    resultados = PantallaResultados()
    for dx in diagnosticos:
        recomendaciones = bridge.obtener_recomendaciones(dx['condicion'])
        resultados.mostrar(dx, recomendaciones)

if __name__ == '__main__':
    main()
```

---

## Flujo Visual Completo

```
┌─────────────────────────────────────────────────────────┐
│                     PYTHON (UI)                         │
│                                                         │
│  main.py                                                │
│    │                                                    │
│    ├─ Muestra bienvenida                                │
│    │                                                    │
│    ├─ Fase 1: muestra G1..G15 uno por uno               │
│    │    └─ Por cada respuesta:                          │
│    │         bridge.guardar_respuesta(id, valor)        │
│    │              │                                     │
│    │              ▼                                     │
│    │    ┌─────────────────────────────────────────┐     │
│    │    │         PROLOG                          │     │
│    │    │  assertz(respuesta(g1, 3)).             │     │
│    │    │  assertz(respuesta(g2, 4)).  ...        │     │
│    │    └─────────────────────────────────────────┘     │
│    │                                                    │
│    ├─ bridge.obtener_modulos_activos()                  │
│    │         │                                          │
│    │         ▼                                          │
│    │    ┌─────────────────────────────────────────┐     │
│    │    │         PROLOG                          │     │
│    │    │  modulos_activos(M) →                  │     │
│    │    │    findall(X, activar_modulo(X), M)    │     │
│    │    │  Retorna: [ansiedad, depresion]         │     │
│    │    └─────────────────────────────────────────┘     │
│    │                                                    │
│    ├─ Fase 2: para cada módulo activo                   │
│    │    ├─ bridge.obtener_preguntas_modulo(mod)         │
│    │    │    → Prolog devuelve lista de textos          │
│    │    └─ Por cada respuesta:                          │
│    │         bridge.guardar_respuesta(id, valor)        │
│    │                                                    │
│    └─ bridge.obtener_diagnosticos()                     │
│              │                                          │
│              ▼                                          │
│    ┌─────────────────────────────────────────┐          │
│    │         PROLOG                          │          │
│    │  diagnostico_completo(C, Puntaje, Nivel)│          │
│    │  → suma respuestas del módulo           │          │
│    │  → aplica nivel_diagnostico/3           │          │
│    │  Retorna: [{condicion: ansiedad,        │          │
│    │             puntaje: 22, nivel: alto}]  │          │
│    └─────────────────────────────────────────┘          │
│                                                         │
│    Muestra resultados bonitos con colores, íconos, etc. │
└─────────────────────────────────────────────────────────┘
```

---

## Resumen: ¿Qué hace cada quien?

| Tarea | Python | Prolog |
|---|---|---|
| Mostrar preguntas con diseño | ✅ | ❌ |
| Guardar respuesta del usuario | ✅ (`assertz`) | ❌ |
| Decidir qué módulos activar | ❌ | ✅ (`activar_modulo`) |
| Saber qué preguntas hacer en Fase 2 | ❌ | ✅ (`pregunta_modulo`) |
| Sumar puntajes | ❌ | ✅ (`puntaje_modulo`) |
| Determinar nivel de diagnóstico | ❌ | ✅ (`nivel_diagnostico`) |
| Mostrar diagnóstico con colores | ✅ | ❌ |
| Guardar recomendaciones | ❌ | ✅ (hechos) |
| Mostrar recomendaciones | ✅ | ❌ |

---

## Instalación necesaria

```bash
# 1. Instalar SWI-Prolog (Mac)
brew install swi-prolog

# 2. Instalar pyswip
pip install pyswip

# 3. Para interfaz gráfica con tkinter (ya viene con Python)
# o si prefieres web:
pip install flask
```

---

*Documento de arquitectura — Sistema Experto Psicológico Python + Prolog — 2026*
