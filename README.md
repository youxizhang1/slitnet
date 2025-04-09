# SlitNET
SlitNet is a deep learning model designed to enhance the spectral resolution of dispersive spectrometers. Initially, we trained the neural network on synthetic data simulating Raman spectra, enabling it to reconstruct high-resolution spectra from low resolution spectra. We then applied transfer learning to adapt the model from synthetic to experimental Raman data of various materials. By fine-tuning the model with experimental measurements, we recovered high-resolution Raman spectra and distinguished between materials that were previously indistinguishable using a wide slit.
## Installation 
The SpectrAI library is used for training and evaluation. Please refer to https://github.com/conor-horgan/spectrai
## Usage
Please refer to https://github.com/conor-horgan/spectrai

Generate synthetic data:
```python
python synthetic_data_generation.py
```
Train the model:
```python
python train.py  --config custom_config.yml --verbose
```
Evaluate results:
```python
python apply.py  --config custom_config.yml
```

The commands above will operate on default configurations that can be found in the config folder.   

Step 1 : Generation of synthetic data 

Step 2 : Training of a model on synthetic data 

Step 3 : Testing on synthetic data and/or experimental data (e.g., polystyrene)

Step 4 : Transfer learning using experimental low and high resolution Raman spectra to improve performance 

Step 5 : Evaluation of model on experimental data (e.g., polystyrene, compounds of Urea and L-Arginine, compounds of Stearic acid, Glycine and L-Methionine)

## Data

Synthetic training data (pair of low and high resolution spectra)

Synthetic testing data (pair of low and high resolution spectra)

Experimental data for testing [i.e., polystyrene] (pair of low and high resolution spectra)

Experimental data for transfer learning (pair of low and high resolution spectra)

Experimental data for testing (pair of low and high resolution spectra)

## Environment
SlitNET was developed using SpectrAI and was implemented and tested in Python 3.8.10 using PyTorch 2.1.0 on a desktop computer with a Core i7-8700 CPU at 3.2 GHz (Intel), 64 GB of RAM, and a Titan V GPU (NVIDIA), running Windows 10 (Microsoft). SpectrAI has not yet been extensively tested in other environments (it's on our to do list).
