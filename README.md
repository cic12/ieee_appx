# Appendix

## Human Leg Muscles

![alt text](https://github.com/cic12/ieee_appx/blob/main/fig_leg_muscles.png "Human Leg Muscles")

Muscles of the thigh segment of the human leg. Muscles targeted for muscle activity sensing are highlighted: a) Vastus Medialis -- VM, b) Rectus Femoris -- RF, c) Biceps Femoris -- BF, and d) Semitendinosus -- SE.

## Dynamic Extension and Flexion Trajectories

[fig_hte_traj.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_traj.pdf)

Knee joint angle and velocity reference trajectories for low, medium, and high frequency repetitions of exercise 2: dynamic extension and flexion. During extension the joint angle increases from 0.2 rad to 1.2 rad and during flexion it decreases back to 0.2 rad.

## Human Torque Prediction Datasets

### Test 1

[fig_hte_mmg_iso_dataset.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_mmg_iso_dataset.pdf)

Human torque prediction dataset for test 1, with processed MMG muscle activity, system states of knee joint angle, $\theta$, and angular velocity, $\dot{\theta}$, and reference human joint torque, $\tau_{\mathrm{ref}}$, recorded during exercise 1: isometric contraction.

### Test 2

[fig_hte_emg_iso_dataset.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_emg_iso_dataset.pdf)

Human torque prediction dataset for test 2 with processed EMG muscle activity, system states of knee joint angle, $\theta$, and angular velocity, $\dot{\theta}$, and reference human joint torque, $\tau_{\mathrm{ref}}$, recorded during exercise 1: isometric contraction.

### Test 3

[fig_hte_mmg_dyn_dataset.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_mmg_dyn_dataset.pdf)

Human torque prediction dataset for test 3 with processed MMG muscle activity, system states of knee joint angle, $\theta$, and angular velocity, $\dot{\theta}$, and reference human joint torque, $\tau_{\mathrm{ref}}$, recorded during exercise 2: dynamic extension and flexion.

### Test 4

[fig_hte_emg_dyn_dataset.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_emg_dyn_dataset.pdf)

Human torque prediction dataset for test 4 with processed EMG muscle activity, system states of knee joint angle, $\theta$, and angular velocity, $\dot{\theta}$, and reference human joint torque, $\tau_{\mathrm{ref}}$, recorded during exercise 2: dynamic extension and flexion.

## Linear and Polynomial Regression Model Fitting Code

[hte_models_listing.py](https://github.com/cic12/ieee_appx/blob/main/hte_model_nn_listing.py)

## Neural Network Model Training Code

[hte_model_nn_listing.py](https://github.com/cic12/ieee_appx/blob/main/hte_model_nn_listing.py)

## Neural Network Training

[fig_hte_nn_training_emg_all.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_nn_training_emg_all.pdf)

Neural network learning curve for the training and validation subsets of the full EMG dataset.

[fig_hte_nn_training_mmg_all.pdf](https://github.com/cic12/ieee_appx/blob/main/fig_hte_nn_training_mmg_all.pdf)

Neural network learning curve for the training and validation subsets of the full MMG dataset.