# CSPC Coursework
## PW1 --- Lab B

The observed decay data showed a clear exponential decrease in count with time.

The observed data matched the analytical law reasonably well: the observed points and the analytical curve showed the same overall exponential decay shape, with small deviations of the measured points from the theoretical curve.

The Snakemake pipeline takes `decay_observed.csv` as input, runs `plot.py`, and produces `figure.png`; it reruns the plotting step when the inputs are newer than the output.
