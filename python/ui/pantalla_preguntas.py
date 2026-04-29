"""
pantalla_preguntas.py
Frames de preguntas y alertas — todos viven dentro de la ventana principal.
Cada frame llama a on_respuesta(id_pregunta, valor) cuando el usuario elige.
"""

import customtkinter as ctk

# ── Paleta ─────────────────────────────────────────────────────────────────────
AZUL_OSCURO  = "#0D1B2A"
AZUL_MEDIO   = "#1B2A4A"
AZUL_CARD    = "#162035"
ACENTO       = "#4F8EF7"
TEXTO_CLARO  = "#E8EDF5"
TEXTO_GRIS   = "#8A9ABB"
VERDE_SUAVE  = "#34C98A"
ROJO_ALERTA  = "#E05C5C"

COLORES_LIKERT = ["#34C98A", "#8BC34A", "#F5A623", "#FF7043", "#E05C5C"]
ETIQUETAS_ESCALA = ["Nunca", "Casi nunca", "A veces", "A menudo", "Siempre"]


class FramePregunta(ctk.CTkFrame):
    """
    Muestra una pregunta con escala Likert.
    Llama a on_respuesta(id_pregunta, valor: int) al seleccionar.
    color_fase: 'azul' (fase 1) | 'verde' (módulos específicos)
    """

    def __init__(self, master, id_pregunta, texto, numero, total,
                 fase, on_respuesta, color_fase="azul"):
        super().__init__(master, fg_color=AZUL_OSCURO, corner_radius=0)
        self._id = id_pregunta
        self._on_respuesta = on_respuesta
        self._respondido = False   # evita doble click

        color_acento = ACENTO if color_fase == "azul" else VERDE_SUAVE
        self._construir(texto, numero, total, fase, color_acento)

    def _construir(self, texto, numero, total, fase, color_acento):
        # ── Barra superior ─────────────────────────────────────────────────────
        barra = ctk.CTkFrame(self, fg_color=AZUL_MEDIO, height=64, corner_radius=0)
        barra.pack(fill="x")
        barra.pack_propagate(False)

        ctk.CTkLabel(
            barra, text=fase,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color=color_acento,
        ).pack(side="left", padx=20)

        ctk.CTkLabel(
            barra, text=f"Pregunta {numero} / {total}",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=TEXTO_GRIS,
        ).pack(side="right", padx=20)

        # ── Barra de progreso ──────────────────────────────────────────────────
        barra_prog = ctk.CTkProgressBar(
            self, fg_color=AZUL_MEDIO, progress_color=color_acento,
            height=5, corner_radius=0,
        )
        barra_prog.pack(fill="x")
        barra_prog.set(numero / total)

        # ── Área central ───────────────────────────────────────────────────────
        centro = ctk.CTkFrame(self, fg_color="transparent")
        centro.pack(fill="both", expand=True, padx=60, pady=24)

        ctk.CTkLabel(
            centro, text=f"{numero:02d}",
            font=ctk.CTkFont(family="Segoe UI", size=48, weight="bold"),
            text_color=color_acento,
        ).pack(anchor="w")

        ctk.CTkLabel(
            centro, text=texto,
            font=ctk.CTkFont(family="Segoe UI", size=17),
            text_color=TEXTO_CLARO, wraplength=640, justify="left",
        ).pack(anchor="w", pady=(6, 28))

        # ── Botones Likert ─────────────────────────────────────────────────────
        self._botones = []
        for i, etiqueta in enumerate(ETIQUETAS_ESCALA):
            btn = ctk.CTkButton(
                centro, text=etiqueta,
                font=ctk.CTkFont(family="Segoe UI", size=13),
                fg_color=AZUL_CARD, hover_color=COLORES_LIKERT[i],
                text_color=TEXTO_GRIS, border_color=AZUL_MEDIO,
                border_width=2, corner_radius=10, height=48,
                command=lambda v=i: self._elegir(v),
            )
            btn.pack(fill="x", pady=4)
            self._botones.append(btn)

        ctk.CTkLabel(
            centro,
            text="Selecciona la opción que mejor describa tu experiencia",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXTO_GRIS,
        ).pack(pady=(16, 0))

    def _elegir(self, valor):
        if self._respondido:
            return
        self._respondido = True

        # Resaltar selección
        for i, btn in enumerate(self._botones):
            if i == valor:
                btn.configure(fg_color=COLORES_LIKERT[i], text_color="#FFF",
                              border_color=COLORES_LIKERT[i])
            else:
                btn.configure(fg_color=AZUL_CARD, text_color=TEXTO_GRIS,
                              border_color=AZUL_MEDIO)

        # Pequeña pausa visual (220 ms) antes de avanzar
        self.after(220, lambda: self._on_respuesta(self._id, valor))


class FrameAlerta(ctk.CTkFrame):
    """Alerta de crisis que reemplaza el frame actual (sin ventana extra)."""

    def __init__(self, master, on_continuar):
        super().__init__(master, fg_color=AZUL_OSCURO, corner_radius=0)
        self._on_continuar = on_continuar
        self._construir()

    def _construir(self):
        inner = ctk.CTkFrame(self, fg_color=AZUL_CARD, corner_radius=16)
        inner.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.55)

        ctk.CTkLabel(
            inner, text="⚠️  Atención",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color=ROJO_ALERTA,
        ).pack(pady=(32, 8))

        ctk.CTkLabel(
            inner,
            text=(
                "Tus respuestas sugieren que podrías estar\n"
                "pasando por un momento muy difícil.\n\n"
                "Si tienes pensamientos de hacerte daño,\n"
                "por favor busca ayuda profesional de inmediato."
            ),
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXTO_GRIS, justify="center",
        ).pack(padx=24, pady=(0, 24))

        ctk.CTkButton(
            inner, text="Entendido, continuar",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color=ROJO_ALERTA, hover_color="#B04040",
            corner_radius=10, height=42,
            command=self._on_continuar,
        ).pack(pady=(0, 28))


class FrameMensajeFinal(ctk.CTkFrame):
    """Mensaje cuando no se activa ningún módulo específico."""

    def __init__(self, master, texto):
        super().__init__(master, fg_color=AZUL_OSCURO, corner_radius=0)
        self._construir(texto)

    def _construir(self, texto):
        inner = ctk.CTkFrame(self, fg_color="transparent")
        inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(inner, text="✅", font=ctk.CTkFont(size=64)).pack(pady=(0, 12))
        ctk.CTkLabel(
            inner, text=texto,
            font=ctk.CTkFont(family="Segoe UI", size=16),
            text_color=VERDE_SUAVE, wraplength=500, justify="center",
        ).pack()
