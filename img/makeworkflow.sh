#!/bin/sh

pdflatex workflow
pdfcrop workflow
mv workflow-crop.pdf workflow.pdf
