import random
import numpy as np
from scipy import io
from scipy.special import wofz
import matplotlib.pyplot as plt


## sets of spectra
N_sets = 20

## pixels in each spectrum
N_points = 1340                                         ## pixels number in spectrometer pixis 400 PI
lambda_low = 212
lambda_high = 2319
x = np.linspace(lambda_low, lambda_high, N_points)      ## raman shift x

## matrix to store spectra (sets*pixels), target/ input / input+noise / original linewidth
Y_TARGET = np.zeros((N_sets, N_points))
Y_INPUT = np.zeros((N_sets, N_points))
Y_INPUT_WN = np.zeros((N_sets, N_points))
Y_ORIGINAL =np.zeros((N_sets, N_points))

## loop for creating each spectrum (ii) (natural linewidth(original)/ target / input / input +noise )
for ii in range(N_sets):
    N_peaks = np.random.randint(25,50)        ## set random numbers of peaks
    mean = np.zeros(N_peaks)                            ## to store random MEANs of each peak
    h = np.zeros(N_peaks)                               ## to store random HEIGHT of each peak
    sd_target = np.zeros(N_peaks)                       ## to store standard deviation (sd) of target
    sd_input = np.zeros(N_peaks)                        ## to store sd for input
    sd_ratio = 3.4                                      ## ratio of input and target sd (resolution), constant for now
    y_original = np.zeros(N_points)
    y_target = np.zeros(N_points)
    y_input = np.zeros(N_points)

    ## loop for creating each peak (i)
    for i in range(N_peaks):
        ## set random mean
        mean[i] = random.randint(lambda_low, lambda_high)

        ## set random height for each peak h[i]
        h[i] = random.random()

        ## create natural linewidth (lorentzian)
        gamma = random.randint(3, 30)             ## to pick a random sd for each peak
        y_o=gamma/(np.pi*(x-mean[i])**2+gamma**2)       ## lorentzian distribution fomula (natual linewidth) for each peak
        y_original = y_original+y_o/max(y_o)*h[i]       ## sum of all peaks ( y_original : natural linewidth for all peaks

        ## set random s.d. for both target + input
        sd_target[i] = 3.4                              ## standard deviation of target
        sd_input[i] = sd_target[i]*sd_ratio             ## standard deviation of input

        ## create target and input , according to voigt function fomula (convolution of lorentzian natural linewidth + gaussian slit effect)
        y_t = np.real(wofz((x - mean[i] + 1j * gamma) / sd_target[i] / np.sqrt(2))) / sd_target[i] \
              / np.sqrt(2 * np.pi)                      ## voigt fomula (target spectrum) for each peak
        y_target = y_target + y_t / max(y_t) * h[i]     ## sum of all peaks : total target spectrum for all peaks
        y_i = np.real(wofz((x - mean[i] + 1j * gamma) / sd_input[i] / np.sqrt(2))) / sd_input[i] \
              / np.sqrt(2 * np.pi)                      ## voigt fomula (input spectrum) for each peaks
        y_input = y_input + y_i / max(y_i) * h[i]       ## sum of all peaks : total input spectrum for all peaks

    ## Normalization
    y_target = y_target / max(y_input)
    y_input = y_input / max(y_input)
    y_original = y_original /max(y_original)


    ## Enlarged to real size
    y_input = y_input * (10 ** 5)
    y_target = y_target * (10 ** 5)

    ## Add noise (shot noise , readout, dark current )
    sigma_shot_noise = np.sqrt(y_input)                 ## shot noise sd proportional to signal size
    sigma_readout = np.random.uniform(10, 700,N_points)
    sigma_dark_current = np.random.uniform(10, 700,N_points)
                                                        ## readout / dark curretn noise are randomly chosen
    sigma_total_noise = np.sqrt(sigma_readout ** 2 + sigma_dark_current ** 2 + sigma_shot_noise ** 2)
                                                        ## sum up three noise
    y_input_wn = np.random.normal(y_input, sigma_total_noise, N_points)
                                                        ## sum up input spectrum + noise = total input spectrum with noise

    ## Normalisation again
    y_target = y_target / max(y_input_wn)
    y_input = y_input / max(y_input)
    y_input_wn = y_input_wn / max(y_input_wn)

    ## Save data into a matrix
    Y_INPUT[ii,:] =y_input
    Y_INPUT_WN[ii, :] = y_input_wn
    Y_TARGET[ii, :] = y_target
    Y_ORIGINAL[ii,:] = y_original*0.8

    ## print a number after each spectrum has been generation
    print(ii)
    #print(y_original)

## plot graph
for ii in range(20):
    plt.plot(x, Y_TARGET[ii, :], 'r', x,Y_INPUT_WN[ii, :], 'k')
    #plt.plot(x, Y_ORIGINAL[ii, :],'g')
    plt.xlim([lambda_low, lambda_high])
    plt.xlabel('Raman shift cm^(-1)')
    plt.ylabel('Intensity (a.u.)')
    plt.title('Random Spectrum with base')
    plt.legend(["Target", "Input with noise"], loc="upper left")
    plt.grid()
    plt.show()

'''
## save data
io.savemat('./data/test_target_spectra/20240823_target_ratio_3.4_10um_100um.mat', {"data": Y_TARGET})
io.savemat('./data/test_input_spectra/20240823_input_ratio_3.4_10um_100um.mat', {"data": Y_INPUT_WN})
io.savemat('./data/20240823_data(natural_target_input_inputwn)_3.4.mat', {"target": Y_TARGET,'input':Y_INPUT,'input_wn':Y_INPUT_WN,'original':Y_ORIGINAL})
# 20sets - test sets ; 0.1m - training sets

'''
