"""
pantalla_resultados.py
Frame de resultados — vive dentro de la ventana principal (sin CTkToplevel).
Recibe los diagnósticos y recomendaciones ya calculados y los muestra en un scroll.
"""

import customtkinter as ctk

# ── Paleta ─────────────────────────────────────────────────────────────────────
AZUL_OSCURO = "#0D1B2A"
AZUL_MEDIO  = "#1B2A4A"
AZUL_CARD   = "#162035"
ACENTO      = "#4F8EF7"
TEXTO_CLARO = "#E8EDF5"
TEXTO_GRIS  = "#8A9ABB"
VERDE_SUAVE = "#34C98A"

COLOR_NIVEL = {"bajo": "#34C98A", "moderado": "#F5A623",
               "alto": "#FF7043", "muy_alto": "#E05C5C"}
EMOJI_NIVEL = {"bajo": "🟢", "moderado": "🟡", "alto": "🟠", "muy_alto": "🔴"}

NOMBRE_CONDICION = {"ansiedad": "Ansiedad", "depresion": "Depresión",
                    "estres": "Estrés", "duelo": "Duelo",
                    "autoestima": "Autoestima", "tdah": "TDAH"}
EMOJI_CONDICION = {"ansiedad": "😰", "depresion": "😔", "estres": "😤",
                   "duelo": "💔", "autoestima": "🪞", "tdah": "⚡"}
MAX_PUNTAJE = {"ansiedad": 32, "depresion": 32, "estres": 32,
               "duelo": 32, "autoestima": 32, "tdah": 40}


class FrameResultados(ctk.CTkFrame):
    """
    Frame de resultados que se muestra dentro de la ventana principal.
    diagnosticos: lista de dicts {'condicion', 'puntaje', 'nivel'}
    recomendaciones: dict {condicion: [str, ...]}
    """

    def __init__(self, master, diagnosticos: list, recomendaciones: dict):
        super().__init__(master, fg_color=AZUL_OSCURO, corner_radius=0)
        self._construir(diagnosticos, recomendaciones)

    def _construir(self, diagnosticos, recomendaciones):
        # ── Encabezado ─────────────────────────────────────────────────────────
        header = ctk.CTkFrame(self, fg_color=AZUL_MEDIO, height=80, corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(
            header, text="📋  Resultados de tu evaluación",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=TEXTO_CLARO,
        ).pack(side="left", padx=28, pady=20)

        ctk.CTkLabel(
            header, text="Sistema Experto Psicológico",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=TEXTO_GRIS,
        ).pack(side="right", padx=28)

        # ── Área scrollable ────────────────────────────────────────────────────
        scroll = ctk.CTkScrollableFrame(
            self, fg_color="transparent",
            scrollbar_button_color=AZUL_MEDIO,
            scrollbar_button_hover_color=ACENTO,
        )
        scroll.pack(fill="both", expand=True, padx=24, pady=16)

        # ── Tarjetas por diagnóstico ───────────────────────────────────────────
        for dx in diagnosticos:
            self._agregar_tarjeta(scroll, dx, recomendaciones.get(dx["condicion"], []))

        # ── Pie de página ──────────────────────────────────────────────────────
        pie = ctk.CTkFrame(scroll, fg_color=AZUL_MEDIO, corner_radius=12)
        pie.pack(fill="x", pady=12, padx=4)
        ctk.CTkLabel(
            pie,
            text="⚕️  Recuerda: estos resultados son orientativos.\n"
                 "Consulta siempre con un profesional de la salud mental.",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=TEXTO_GRIS, justify="center",
        ).pack(padx=20, pady=14)

        ctk.CTkButton(
            scroll, text="Cerrar",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color=ACENTO, hover_color="#3A72D4",
            corner_radius=10, height=40,
            command=self.master.destroy,
        ).pack(pady=(4, 16))

    def _agregar_tarjeta(self, parent, dx, recomendaciones):
        condicion = dx["condicion"]
        puntaje   = dx["puntaje"]
        nivel     = dx["nivel"]

        color = COLOR_NIVEL.get(nivel, ACENTO)
        nombre = NOMBRE_CONDICION.get(condicion, condicion.capitalize())
        max_pts = MAX_PUNTAJE.get(condicion, 32)

        tarjeta = ctk.CTkFrame(parent, fg_color=AZUL_CARD, corner_radius=14,
                               border_width=1, border_color=AZUL_MEDIO)
        tarjeta.pack(fill="x", pady=8, padx=4)

        # Cabecera
        cab = ctk.CTkFrame(tarjeta, fg_color="transparent")
        cab.pack(fill="x", padx=20, pady=(16, 8))

        ctk.CTkLabel(
            cab,
            text=f"{EMOJI_CONDICION.get(condicion, '🔷')}  {nombre}",
            font=ctk.CTkFont(family="Segoe UI", size=17, weight="bold"),
            text_color=TEXTO_CLARO,
        ).pack(side="left")

        ctk.CTkLabel(
            cab,
            text=f"{EMOJI_NIVEL.get(nivel, '⚪')}  {nivel.replace('_', ' ').capitalize()}",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color=color,
        ).pack(side="right")

        # Puntaje y barra
        pts_frame = ctk.CTkFrame(tarjeta, fg_color="transparent")
        pts_frame.pack(fill="x", padx=20, pady=(0, 8))

        ctk.CTkLabel(
            pts_frame, text=f"Puntaje:  {puntaje} / {max_pts}",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=TEXTO_GRIS,
        ).pack(anchor="w")

        barra = ctk.CTkProgressBar(pts_frame, fg_color=AZUL_MEDIO,
                                   progress_color=color, height=8, corner_radius=4)
        barra.pack(fill="x", pady=(4, 0))
        barra.set(puntaje / max_pts)

        # Recomendaciones
        if recomendaciones:
            ctk.CTkFrame(tarjeta, height=1, fg_color=AZUL_MEDIO).pack(fill="x", padx=20, pady=8)
            ctk.CTkLabel(
                tarjeta, text="💡  Recomendaciones",
                font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
                text_color=ACENTO,
            ).pack(anchor="w", padx=20, pady=(0, 6))

            for rec in recomendaciones:
                rec_frame = ctk.CTkFrame(tarjeta, fg_color=AZUL_MEDIO, corner_radius=8)
                rec_frame.pack(fill="x", padx=20, pady=3)
                ctk.CTkLabel(
                    rec_frame, text=f"→  {rec}",
                    font=ctk.CTkFont(family="Segoe UI", size=12),
                    text_color=TEXTO_GRIS, wraplength=660, justify="left",
                ).pack(anchor="w", padx=12, pady=8)

        ctk.CTkFrame(tarjeta, height=10, fg_color="transparent").pack()
