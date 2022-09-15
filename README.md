# Pinnacle_LARK_Dose_Recon

## Purpose
To compare dose distributions with and without LARK tracking for Pinnacle Treatment Planning System

## Method
This project is written with Pinnacle Script and Python 2.7.9. It converts VMAT beams to 2 degrees gantry separation. And then splits each control ponit of each VMAT beam into a single static beam with the energy, MU, field aperture and MLC positions, gantry/collimator/couch angles from the control point. Two trails with_LARK and without_LARK will be created. The isocentre for each static beam will be shifted based on Tracking Files generated from LARK treatment procedure. The dose distribution for both trials will be re-calculated.

## Requirements
* Traking Files format:
	* Must named as "BeamName_with_LARK" and "BeamName_without_LARK" (replace BeamName with your real beam name).
	* The first row is the title separated by Tab "Bin	Gantry	x	y	z (Pinnacle, mm)".
	* From the second row, the data should be co-related with title and separated by Tab.
* This project is heavy workloaded. Please run it when Pinnacle is free. Running after hour is recommanded.

## Instruction of use
* Copy all source files to Pinnacle "/usr/local/adacnew/PinnacleSiteData/Scripts/HotScripts/Physics/LARK_Dose_Recon_v1.4/".
* Make sure this folder and sub-folder have write permission for users.
* Copy Tracking files with right names and format to Pinnacle "/home/p3rtp/RadCalc/LARK/".
* Run the initial script "start.Script" under the path "/usr/local/adacnew/PinnacleSiteData/Scripts/HotScripts/Physics/LARK_Dose_Recon_v1.4/".
* The procedure can be hours depends on the clinical plan and Pinnacle workload. 
* The procedure is finihsed when the script window closed.
* Each fraction must run in a new copied clinical plan. After reconstruction done, the dose and ROIs can be exported to Velocty.
* Dose summary for the course can be done in Velocity.
