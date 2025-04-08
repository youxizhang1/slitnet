# SlitNet
SlitNet is a spectrometer slit empowered by a deep learning model, that can enhance spectral resolution and signal-to-noise ratio from low-resolution inputs. Using synthetic data resembling Raman spectra, we trained a neural network to reconstruct synthetic Raman spectra with enhanced resolution and signal-to-noise ratio from low-resolution inputs. Subsequently, we performed transfer learning from synthetic data to experimental Raman data of materials. Through fine-tuning the model with experimental data, we successfully recovered high resolution Raman spectra and discriminated between two materials that were previously indistinguishable using a wide slit.
## Installation 
Spectrai library is used for training and evaluation. Please refer to https://github.com/conor-horgan/spectrai
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

The commands above will operate on default configs , from which six steps of model optimization could be achieved.   

0.  Generating synthetic data 
1.	Training on synthetic data 
2.	Applying on synthetic data and experimental data ( Polystyrene )
3.	Transfer learning on chemicals 
4.	Applying on experimental data ( Polystyrene , compounds of Urea and L-Arginine , compounds of Stearic acid, Glycine and L-Methionine )

## Data
1.  Synthetic Training
2.  Experimental Testing (Polystyrene)
2.  Synthetic Testing
3.  Transfer Learning
4.  Testing on biochemical compounds
## Environment
spectrai was implemented and tested in Python 3.8.10 using PyTorch 2.1.0 on a desktop computer with a Core i7-8700 CPU at 3.2 GHz (Intel), 64 GB of RAM, and a Titan V GPU (NVIDIA), running Windows 10 (Microsoft). spectrai has not yet been extensively tested in other environments (it's on our to do list).
