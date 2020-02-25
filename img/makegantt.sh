#!/bin/sh

pdflatex cog-gantt
pdfcrop cog-gantt
mv cog-gantt-crop.pdf cog-gantt.pdf
