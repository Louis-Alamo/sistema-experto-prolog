"""
pantalla_bienvenida.py
Frame de bienvenida — vive dentro de la ventana principal (sin CTkToplevel).
"""

import customtkinter as ctk

AZUL_OSCURO  = "#0D1B2A"
AZUL_MEDIO   = "#1B2A4A"
ACENTO       = "#4F8EF7"
ACENTO_HOVER = "#3A72D4"
TEXTO_CLARO  = "#E8EDF5"
TEXTO_GRIS   = "#8A9ABB"


class FrameBienvenida(ctk.CTkFrame):
    """Frame de bienvenida que llama a on_inicio() cuando el usuario presiona Comenzar."""

    def __init__(self, master, on_inicio):
        super().__init__(master, fg_color=AZUL_OSCURO, corner_radius=0)
        self._on_inicio = on_inicio
        self._construir()
        self._fade_in(0.0)

    def _construir(self):
        self.configure(fg_color=AZUL_OSCURO)
        inner = ctk.CTkFrame(self, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=60, pady=30)

        ctk.CTkLabel(inner, text="🧠", font=ctk.CTkFont(size=72)).pack(pady=(10, 0))

        ctk.CTkLabel(
            inner,
            text="Sistema Experto Psicológico",
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color=TEXTO_CLARO,
        ).pack(pady=(10, 4))

        ctk.CTkLabel(
            inner,
            text="Evaluación inteligente de bienestar emocional",
            font=ctk.CTkFont(family="Segoe UI", size=14),
            text_color=ACENTO,
        ).pack(pady=(0, 20))

        ctk.CTkFrame(inner, height=2, fg_color=AZUL_MEDIO).pack(fill="x", padx=20, pady=(0, 20))

        desc = (
            "Este cuestionario consta de dos fases:\n\n"
            "  🔹  Fase 1 — Evaluación general (15 preguntas)\n"
            "  🔹  Fase 2 — Módulos específicos según tus respuestas\n\n"
            "Al finalizar recibirás un informe con diagnósticos y\n"
            "recomendaciones personalizadas."
        )
        ctk.CTkLabel(
            inner, text=desc,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXTO_GRIS, justify="left",
        ).pack(pady=(0, 20))

        aviso = ctk.CTkFrame(inner, fg_color=AZUL_MEDIO, corner_radius=10)
        aviso.pack(fill="x", padx=10, pady=(0, 24))
        ctk.CTkLabel(
            aviso,
            text="⚠️  Este sistema es una herramienta académica y NO reemplaza\n"
                 "la evaluación de un profesional de la salud mental.",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXTO_GRIS, justify="center",
        ).pack(padx=16, pady=10)

        self._btn = ctk.CTkButton(
            inner,
            text="  Comenzar evaluación  ",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            fg_color=ACENTO, hover_color=ACENTO_HOVER,
            text_color="#FFFFFF", corner_radius=12, height=48,
            command=self._iniciar,
        )
        self._btn.pack()

    def _fade_in(self, alpha):
        try:
            self.master.attributes("-alpha", alpha)
            if alpha < 1.0:
                self.after(18, lambda: self._fade_in(min(alpha + 0.06, 1.0)))
        except Exception:
            pass

    def _iniciar(self):
        self._btn.configure(state="disabled")
        self._fade_out(1.0)

    def _fade_out(self, alpha):
        try:
            self.master.attributes("-alpha", alpha)
            if alpha > 0.0:
                self.after(16, lambda: self._fade_out(max(alpha - 0.08, 0.0)))
            else:
                self.master.attributes("-alpha", 1.0)
                self._on_inicio()
        except Exception:
            self._on_inicio()
