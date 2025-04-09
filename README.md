# SlitNet
SlitNet is a spectrometer slit empowered by a deep learning model, that can enhance spectral resolution and signal-to-noise（SNR) ratio from low-resolution inputs. We first trained a neural network using synthetic data that mimics Raman spectra, enabling it to reconstruct high-resolution spectra with improved SNR. Subsequently, we performed transfer learning from synthetic data to experimental Raman data of materials. Through fine-tuning the model with experimental data, we successfully recovered high resolution Raman spectra and discriminated between two materials that were previously indistinguishable using a conventional wide slit.
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

The commands above will operate on default configs , from which five steps of model optimization could be achieved.   

0.  Generating synthetic data 
1.	Training on synthetic data 
2.	Evaluating on synthetic data and experimental data ( Polystyrene )
3.	Transfer learning on chemicals 
4.	Evaluating on experimental data ( Polystyrene , compounds of Urea and L-Arginine , compounds of Stearic acid, Glycine and L-Methionine )

## Data
1. Synthetic Training
2. Experimental Testing (Polystyrene)
3. Synthetic Testing
4. Transfer Learning
5. Testing on biochemical compounds
## Environment
spectrai was implemented and tested in Python 3.8.10 using PyTorch 2.1.0 on a desktop computer with a Core i7-8700 CPU at 3.2 GHz (Intel), 64 GB of RAM, and a Titan V GPU (NVIDIA), running Windows 10 (Microsoft). spectrai has not yet been extensively tested in other environments (it's on our to do list).
