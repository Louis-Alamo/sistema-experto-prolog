% Carga todos los archivos en orden
:- consult('escala.pl').
:- consult('activacion.pl').
:- consult('modulo_ansiedad.pl').
%:- consult('modulo_depresion.pl'). <- Solo le quitas el simbolo de porcentaje
%:- consult('modulo_estres.pl').
:- consult('modulo_duelo.pl').
%:- consult('modulo_autoestima.pl').
:- consult('modulo_tdah.pl').
:- consult('diagnostico.pl').
:- consult('recomendaciones.pl').
% Las respuestas son dinámicas (Python las inserta en tiempo de ejecución)
:- dynamic respuesta/2.
