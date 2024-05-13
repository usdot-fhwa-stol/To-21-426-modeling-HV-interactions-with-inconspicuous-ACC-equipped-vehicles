# Summary
This repository contains the source code of calibrating IDM model for human-driven vehicles (HVs) when they follow HVs and when they follow Advanced Driver Assistance System (ADAS) – equipped vehicles. 
The source code was developed to obtain the IDM parameters of HVs under the two following scenarios. Based on the calibrated results, the relationships between IDM parameters when HVs follow HVs and ADAS-equipped 
vehicles are determined. This repository also includes the source code of a mixed traffic simulation model. The mixed traffic simulation model includes two types of vehicles: HVs and ADAS-equipped vehicles. 
Both vehicle categories relied on the IDM model to govern their behavior when following other vehicles. The IDM parameter for ADAS-equipped vehicles and for HVs when they follow other HVs are based on the existing 
studies. To demonstrate the effects of HVs on the road network when they follow ADAS-equipped vehicles using the calibrated IDM model, two distinct scenarios were examined. In the first scenario, the specific IDM 
model parameters determined by the developed parameter relationships was used to define HVs following ADAS-equipped vehicles. In the second scenario, there was no specialized IDM model for HVs following ADAS-equipped 
vehicles. The simulation was conducted in Eclipse® Simulation of Urban Mobility (SUMO) and the source code was programmed in Pycharm.
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
* SUMO 1.16.0
* Pycharm 2022.3.2
* Anoconda
# Usage
## Installing software tools
* Install SUMO 1.16.0
* Install Pycharm
* Install Anoconda
## Testing
### Car-following model calibration
Step 1: Open Jupyter notebook in Anoconda
Step 2: Upload the file “PSO algorithm for calibration” onto your Jupyter notebook.
Step 3: If you’d like to obtain parameters for the scenario of HVs following HVs, you need to set “CAV_judge = False” in the code. If you’d like to obtain parameters for the scenario of HVs following ADAS-equipped vehicles, you need to set “CAV_judge= True” in the code.
Step 4: After setting this parameter, click “Run” under kernel to run each block continuously or click “Restart & Run all” under kernel to run all the blocks all the time. 
### Simulation
Step 1: Open Pycharm
Step 2: Use Pycharm to open the “generate_sumo_files.py” and “runner.py”. 
Step 3: Click the run button to run the file of “runner.py” to start the simulation.
Step 4:  After the simulation, the trip information can be generated and saved in the file with ‘.xml’ extension. 
# License
This project is licensed under the Apache 2.0 License.
# Acknowledgements
This research is supported by Federal Highway Administration (FHWA) Office of Operations Research and Development HRDO program under the project entitled Developing Improved Analysis, 
Modeling, and Simulation Tools for Advanced Driver Assistance Systems and Automated Driving System Applications.
