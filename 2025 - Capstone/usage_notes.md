# Usage Notes

## New Build

For `project.tex`:
Delete files named `<project>.*`,
not named `project.tex`

`pdflatex -> makeglossaries -> pdflatex x2`

then:

`pdflatex -> biber -> pdflatex x2`
