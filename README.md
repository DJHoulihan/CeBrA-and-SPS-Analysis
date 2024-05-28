# A guide for data analysis on the SE-SPS and CeBrA

This is a set of jupyter notebooks with the aim of guiding experimenters on how to analyze data from experiments involving the SE-SPS and CeBrA. The guide includes instructions on how to perform energy calibration for both the SE-SPS and CeBrA, to gain-match and combine the CeBrA spectra, and to normalize and combine SE-SPS data with differing magnetic field settings. The end goal is to create a particle-gamma coincidence matrix that is fully energy-calibrated. For the user, the procedure is outlined completely in 'cebra_sps_analysis.ipynb' with 'xavgnormalization.ipynb' and 'checkinggainmatch.ipynb' providing supplementary code for checking one's work. The following programs are necessary for this analysis, with the installation included in the github accounts listed.

## Programs Used

1. HDTV: https://github.com/janmayer/hdtv
2. SPS_CeBrA_EventBuilder: https://github.com/alconley/SPS_CEBRA_EventBuilder
   
## System Requirements

For HDTV:
- To build and run HDTV, the following dependencies are required:
    Python
        Tested with 3.8, 3.9, 3.10, and 3.11
        Python-dependencies are installed automatically when using pip/pipx
            Packages: numpy scipy matplotlib prompt_toolkit>=3.0.14 uncertainties (when manually installed)
            Packages for development & testing: docutils pytest pytest-cov
    Cern ROOT 6
        Tested with version 6.26 and higher
        Needs to be compiled against the correct python version and with support for C++14 or higher.
        In python, import ROOT must succeed.
        System packages may be available on some systems, e.g. <tool> install root python3-root (More info)
    cmake, gcc, g++ (or similar, in a somewhat modern version)
    libx11-dev <tool> install libx11-6 libx11-dev

For python analysis:
- Python 3.8 or greater
  
For EventBuilder:
- Requires ROOT >= 6.22.04 for C++17 support
- Requires CMake > 3.16 for pch suport
- This version is for data from CAEN CoMPASS > 2.0. Data from older CoMPASS versions are not compatible.
