# CSPC Coursework
## PW1 --- Lab B

The observed decay data showed a clear exponential decrease in count with time.

The observed data matched the analytical law reasonably well: the observed points and the analytical curve showed the same overall exponential decay shape, with small deviations of the measured points from the theoretical curve.

The Snakemake pipeline takes `decay_observed.csv` as input, runs `plot.py`, and produces `figure.png`; it reruns the plotting step when the inputs are newer than the output.


## PW2 --- Lab A

### Results

The mean acceleration measured from the noisy position data was
-8.580 m/s^2, which is reasonably close to the expected gravitational
acceleration of -9.81 m/s^2.

The acceleration was very noisy because numerical differentiation
amplifies measurement noise. The acceleration standard deviation was
28.716 m/s^2.

Integrating the noisy acceleration back twice recovered the position
reasonably well. The largest difference between the recovered and
original position was 0.785 m, which is less than 1 m. This shows that
integration suppresses noise compared with differentiation.

The final figure `motion.png` contains position, velocity, and
acceleration versus time, with the true -9.81 m/s^2 acceleration shown
as a dashed reference line.
