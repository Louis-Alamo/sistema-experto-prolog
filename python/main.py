"""
main.py — Sistema Experto Psicológico
Arquitectura: ventana única, flujo 100% event-driven (sin hilos).
Todos los frames viven dentro de la misma CTk root.

Modos:
  python main.py          → Prolog real (requiere pyswip + SWI-Prolog)
  python main.py --demo   → PrologBridgeMock (sin Prolog)
"""

import sys
import customtkinter as ctk

from prolog_bridge import PrologBridge, PrologBridgeMock
from ui.pantalla_bienvenida import FrameBienvenida
from ui.pantalla_preguntas import FramePregunta, FrameMensajeFinal
from ui.pantalla_resultados import FrameResultados

# ── Configuración global ───────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── Preguntas generales (Fase 1) ───────────────────────────────────────────────
PREGUNTAS_GENERALES = [
    ("g1",  "¿Con qué frecuencia te sientes triste o con el ánimo muy bajo?"),
    ("g2",  "¿Con qué frecuencia sientes que te preocupas demasiado?"),
    ("g3",  "¿Con qué frecuencia sientes que no tienes energía?"),
    ("g4",  "¿Con qué frecuencia tu estado de ánimo afecta tu vida diaria?"),
    ("g5",  "¿Con qué frecuencia te sientes irritable sin razón clara?"),
    ("g6",  "¿Con qué frecuencia tienes dificultad para dormir?"),
    ("g7",  "¿Con qué frecuencia sientes tensión muscular o dolor de cabeza?"),
    ("g8",  "¿Con qué frecuencia ha cambiado tu apetito?"),
    ("g9",  "¿Con qué frecuencia te cuesta concentrarte?"),
    ("g10", "¿Con qué frecuencia dejas tareas sin terminar?"),
    ("g11", "¿Con qué frecuencia tu mente salta de pensamiento en pensamiento?"),
    ("g12", "¿Con qué frecuencia te has alejado de personas cercanas?"),
    ("g13", "¿Con qué frecuencia perdiste interés en actividades que antes disfrutabas?"),
    ("g14", "¿Con qué frecuencia sientes que no vales lo suficiente?"),
    ("g15", "¿Con qué frecuencia has tenido una pérdida importante recientemente?"),
]


# ── Aplicación principal ───────────────────────────────────────────────────────

class App(ctk.CTk):
    """
    Ventana única que gestiona todo el flujo del cuestionario.
    Los 'estados' son frames que se destruyen y reemplazan dentro de esta misma ventana.
    No se crean ventanas secundarias (CTkToplevel) en ningún momento.
    """

    def __init__(self, bridge):
        super().__init__()
        self.bridge = bridge
        self.title("Sistema Experto Psicológico")
        self.geometry("760x600")
        self.resizable(False, False)

        self.update_idletasks()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"760x600+{(sw-760)//2}+{(sh-600)//2}")

        self._frame_actual = None
        self._ir_a(FrameBienvenida(self, on_inicio=self._iniciar_fase1))

    # ── Navegación ─────────────────────────────────────────────────────────────

    def _ir_a(self, frame_nuevo):
        """Destruye el frame visible y muestra el nuevo, todo en la misma ventana."""
        if self._frame_actual is not None:
            self._frame_actual.destroy()
        self._frame_actual = frame_nuevo
        self._frame_actual.pack(fill="both", expand=True)

    # ── Estado: Bienvenida → Fase 1 ────────────────────────────────────────────

    def _iniciar_fase1(self):
        self._idx_g = 0
        self._mostrar_pregunta_general()

    def _mostrar_pregunta_general(self):
        id_p, texto = PREGUNTAS_GENERALES[self._idx_g]
        self._ir_a(FramePregunta(
            self,
            id_pregunta=id_p,
            texto=texto,
            numero=self._idx_g + 1,
            total=len(PREGUNTAS_GENERALES),
            fase="Fase 1 — Evaluación General",
            color_fase="azul",
            on_respuesta=self._on_respuesta_general,
        ))

    def _on_respuesta_general(self, id_pregunta, valor):
        self.bridge.guardar_respuesta(id_pregunta, valor)
        self._idx_g += 1
        if self._idx_g < len(PREGUNTAS_GENERALES):
            self._mostrar_pregunta_general()
        else:
            self._determinar_modulos()

    # ── Estado: Determinar módulos activos ─────────────────────────────────────

    def _determinar_modulos(self):
        self._modulos = self.bridge.obtener_modulos_activos()
        if not self._modulos:
            self._ir_a(FrameMensajeFinal(
                self,
                texto="¡Sin indicios significativos!\nTus respuestas sugieren un estado emocional estable. 🌿\nSigue cuidándote."
            ))
            return
        self._idx_modulo = 0
        self._iniciar_modulo()

    # ── Estado: Fase 2 — Módulos específicos ───────────────────────────────────

    def _iniciar_modulo(self):
        modulo = self._modulos[self._idx_modulo]
        self._modulo_actual = modulo
        self._preguntas_modulo = self.bridge.obtener_preguntas_modulo(modulo)
        self._idx_pregunta_m = 0
        self._mostrar_pregunta_modulo()

    def _mostrar_pregunta_modulo(self):
        pregunta = self._preguntas_modulo[self._idx_pregunta_m]
        nombre_modulo = {
            "ansiedad": "Módulo — Ansiedad",
            "depresion": "Módulo — Depresión",
            "estres": "Módulo — Estrés",
            "duelo": "Módulo — Duelo",
            "autoestima": "Módulo — Autoestima",
            "tdah": "Módulo — TDAH",
        }.get(self._modulo_actual, f"Módulo — {self._modulo_actual.capitalize()}")

        self._ir_a(FramePregunta(
            self,
            id_pregunta=pregunta["id"],
            texto=pregunta["texto"],
            numero=self._idx_pregunta_m + 1,
            total=len(self._preguntas_modulo),
            fase=nombre_modulo,
            color_fase="verde",
            on_respuesta=self._on_respuesta_modulo,
        ))

    def _on_respuesta_modulo(self, id_pregunta, valor):
        self.bridge.guardar_respuesta(id_pregunta, valor)
        # Alerta especial D3
        if id_pregunta == "d3" and self.bridge.alerta_depresion_grave():
            self._mostrar_alerta_crisis(callback=self._continuar_modulo)
            return
        self._continuar_modulo()

    def _continuar_modulo(self):
        self._idx_pregunta_m += 1
        if self._idx_pregunta_m < len(self._preguntas_modulo):
            self._mostrar_pregunta_modulo()
        else:
            self._idx_modulo += 1
            if self._idx_modulo < len(self._modulos):
                self._iniciar_modulo()
            else:
                self._mostrar_resultados()

    # ── Estado: Resultados ─────────────────────────────────────────────────────

    def _mostrar_resultados(self):
        diagnosticos = self.bridge.obtener_diagnosticos()
        recomendaciones = {
            dx["condicion"]: self.bridge.obtener_recomendaciones(dx["condicion"])
            for dx in diagnosticos
        }
        self._ir_a(FrameResultados(self, diagnosticos=diagnosticos, recomendaciones=recomendaciones))

    # ── Alerta de crisis (inline, sin ventana extra) ────────────────────────────

    def _mostrar_alerta_crisis(self, callback):
        from ui.pantalla_preguntas import FrameAlerta
        self._ir_a(FrameAlerta(self, on_continuar=callback))


# ── Punto de entrada ───────────────────────────────────────────────────────────

def main():
    modo_demo = "--demo" in sys.argv
    if modo_demo:
        print("▶  Modo DEMO — usando PrologBridgeMock (sin Prolog)")
        bridge = PrologBridgeMock()
    else:
        print("▶  Modo REAL — conectando con SWI-Prolog via pyswip")
        bridge = PrologBridge()

    app = App(bridge)
    app.mainloop()


if __name__ == "__main__":
    main()
