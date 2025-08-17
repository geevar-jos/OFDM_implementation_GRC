# OFDM_implementation_GRC
GNU radio implementation of OFDM scheme

# Orthogonal Frequency Division Multiplexing (OFDM)

## Introduction
Orthogonal Frequency Division Multiplexing (OFDM) is a **multicarrier modulation scheme** used in modern wireless communication systems.  
It divides the available spectrum into many closely spaced **orthogonal subcarriers**, each carrying a low-rate data stream. By ensuring orthogonality, the subcarriers can **overlap without interfering**, which improves spectral efficiency.  

Key advantages:
- **Efficient spectrum usage** through overlapping subcarriers.  
- **Robustness against multipath fading**, as a wideband channel is split into narrowband subchannels.  
- **Simplified equalization** since each subcarrier experiences flat fading.  
- **Cyclic prefix (CP)** helps mitigate inter-symbol interference (ISI).  
- Widely adopted in standards such as **Wi-Fi, LTE, 5G, DVB, and DSL**.  

---

## OFDM System Flow
At Transmitter : 

Input Data  -> Symbol Mapping (QPSK) -> OFDM Modulation (IFFT → Time Domain) -> Transmitted on Channel (Multipath + AWGN)

At Receiver : 

Received Data from Channel (Multipath + AWGN) -> OFDM Demodulation (FFT → Frequency Domain) -> Symbol Detection -> Output Data + Constellation Visualization
 

## Explanation of Blocks

- **Input Bits**  : The binary data to be transmitted is fed into the OFDM system.

- **Mapping (QAM/PSK)**  : Bits are grouped and mapped into complex-valued modulation symbols using schemes like **QPSK, 16-QAM, or 64-QAM**.

- **IFFT (Inverse Fast Fourier Transform)** : Converts the symbols from the frequency domain into a time-domain OFDM signal. Each subcarrier corresponds to one frequency bin.

- **Add Cyclic Prefix (CP)** : A guard interval is added at the start of each OFDM symbol by copying the last portion of the symbol. This mitigates **inter-symbol interference (ISI)** caused by multipath.

- **Channel** : The transmitted signal passes through a wireless channel which introduces **multipath fading, delay, and noise**.

- **Remove Cyclic Prefix** : At the receiver, the CP is removed to recover the original OFDM symbol length.

- **FFT (Fast Fourier Transform)** : Converts the received time-domain signal back to the frequency domain, recovering the subcarrier symbols.

- **Demapping (QAM/PSK)** : The received symbols are converted back into binary bits, reconstructing the original transmitted data.

- **Output Bits** : Final recovered bitstream, ideally matching the input (with some errors depending on channel noise). 
  
  
# OFDM Simulation Project (GNU Radio)

## Summary
This project implements a **baseband OFDM transceiver** in GNU Radio to demonstrate modulation, channel effects, and symbol recovery.

## Technical details
- **OFDM Parameters**:  
  - FFT size = **8 subcarriers**  
  - Modulation = **QPSK (constellation mapping)**  
  - Random data source mapped to complex symbols  

- **Channel Model**:  
  - Multipath channel with taps:  
    \[
    h = [1,\; 0.2+0.3j,\; 0.1-0.05j]
    \]  
  - **Additive White Gaussian Noise (AWGN)** with adjustable standard deviation (`noise_std`)  

- **Transmitter**:  
  - Random source → QPSK constellation encoder  
  - IFFT converts frequency-domain subcarriers → time-domain OFDM symbols  

- **Receiver**:  
  - FFT recovers frequency-domain subcarriers  
  - Subcarrier outputs visualized on **constellation diagram sink**  

- **Key Demonstrations**:  
  - Effect of **multipath distortion** on OFDM symbols  
  - Impact of **noise level (SNR variation)** on symbol detection  
  - **Visualization** of subcarrier orthogonality and symbol recovery using QT GUI  

## Conclusion
This system provides an **end-to-end OFDM link simulation** that highlights how FFT-based demodulation enables robust symbol recovery in the presence of noise and multipath fading.
