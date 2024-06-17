# Summary
This repository contains the source code of calibrating IDM model for human-driven vehicles (HVs) when they follow HVs and when they follow Advanced Driver Assistance System (ADAS) – equipped vehicles. 
The source code was developed to obtain the IDM parameters of HVs under the two following scenarios. Based on the calibrated results, the relationships between IDM parameters when HVs follow HVs and ADAS-equipped 
vehicles are determined. 
# Outline
* Project Description
* Prerequisites
* Usage
* License
* Contact Information
* Acknowledgements
# Project Description
The project title is Developing Improved Analysis, Modeling, and Simulation Tools for Advanced Driver Assistance Systems and Automated Driving System Applications. The majority of existing AMS tools were 
primarily built to model human driver behavior in the environment that consists of only human-driven vehicles (HVs). This design focus makes them less effective at mimicking automated driving behavior or 
simulating interactions between HVs and AVs. Without these dedicated resources, the tools risk estimating the impacts of ADAS and ADS technologies on traffic flow. Therefore, before these tools can be used 
for accurate simulation study, it is necessary that the current AMS tools evolve to incorporate the complexities of ADAS and ADS capabilities. To achieve this objective, the Federal Highway Administration (FHWA) 
launched this project with the goal of enhancing current AMS tools to improve modeling for ADAS and ADS applications. The majority of existing AMS tools were primarily built to model human driver in the environment 
that consists of only human-driven vehicles (HVs). This design focus on makes them less effective at mimicking automated driving behavior or simulating interactions between HVs and AVs. 
# Prerequisites
* Pycharm 2022.3.2
* Anoconda
# Usage
## Installing software tools
* Install Pycharm
* Install Anoconda
## Testing
### Car-following model calibration
Step 1: Open Jupyter notebook in Anoconda\
Step 2: Upload the file “PSO algorithm for calibration” onto your Jupyter notebook.\
Step 3: If you’d like to obtain parameters for the scenario of HVs following HVs, you need to set “CAV_judge = False” in the code. If you’d like to obtain parameters for the scenario of HVs following ADAS-equipped vehicles, you need to set “CAV_judge= True” in the code.\
Step 4: After setting this parameter, click “Run” under kernel to run each block continuously or click “Restart & Run all” under kernel to run all the blocks all the time. 
# License
This project is licensed under the Apache 2.0 License.
# Contributions

Please read [CONTRIBUTING.md](https://github.com/usdot-jpo-codehub/codehub-readme-template/blob/master/Contributing.MD) for details on our Code of Conduct, the process for submitting pull requests to us, and how contributions will be released.

# Contact Information

Contact Name: Zhitong Huang
Contact Information: Zhitong.Huang@leidos.com
# Acknowledgements
This research is supported by Federal Highway Administration (FHWA) Office.
## Citing this code
To track how this government-funded code is used, we request that if you decide to build additional software using this code please acknowledge its Digital Object Identifier in your software's README/documentation.

> Digital Object Identifier: https://doi.org/xxx.xxx/xxxx

To cite this code in a publication or report, please cite our associated report/paper and/or our source code. Below is a sample citation for this code:

> ITS CodeHub Team. (2021). _ITS CodeHub README Template_ (0.1) [Source code]. Provided by ITS CodeHub through GitHub.com. Accessed 2021-01-27 from https://doi.org/xxx.xxx/xxxx.

When you copy or adapt from this code, please include the original URL you copied the source code from and the date of retrieval as a comment in your code. Additional information on how to cite can be found in the [ITS CodeHub FAQ](https://its.dot.gov/code/#/faqs).
