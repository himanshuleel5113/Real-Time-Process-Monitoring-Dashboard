# Real Time Process Monitoring Dashboard
A real-time process monitoring tool for Windows that provides detailed CPU and memory usage tracking for all running processes.


# Problem Statement
Problem: Real-Time Process Monitoring Dashboard
Description: Create a graphical dashboard that displays real-time information about process states, CPU usage, and memory consumption. The tool should allow administrators to manage processes efficiently and identify potential issues promptly.


# Features

 # Process Monitoring
 Real-time monitoring of all system processes
 
 CPU usage tracking with percentage display
 
 Memory usage monitoring in MB/GB
 
 System-wide resource usage overview
 
 Process filtering and sorting capabilities
 
 Modern ImGui-based user interface

 # Process Management
 
 Process termination capability
 
 Process priority control (Idle, Below Normal, Normal, Above Normal, High, Real-time)
 
 Process suspension and resumption
 
 Process path and elevation status information

  # Resource Monitoring
  
 Total system CPU utilization tracking
 
 Total and available memory monitoring
 
 Per-process resource usage statistics
 
 High resource usage detection and alerts

  # Alert System
  
 Configurable CPU and memory usage thresholds
 
 Consecutive high usage detection
 
 Customizable alert timeout settings
 
 Process-specific alert tracking

 
# Security Features

 Process privilege verification
 
 Elevated process detection
 
 Secure process management with proper access controls


#Working:-

 # Data Collection:-

 The data_collection.py script gathers the system data like CPU, memory and processes using psutil library.
 The data collected by data_collection.py script saved into system_matrics.json file so that dashboard can access.

# Dashboard:-

The dashboard.py script reads the data from system.matrics.json file and show on dashboard.
User can can see the running process and CPU usage details on the deshboard in a interactive way.


# Usage


 # Basic Operations
 
 View all running processes with their resource usage
 
 Sort processes by CPU usage, memory usage, or name
 
 Monitor system-wide resource utilization

 # Process Management
 
 Right-click on processes to access management options
 
 Change process priorities
 
 Suspend/Resume processes
 
 Terminate processes (requires appropriate privileges)

# Alert Configuration
 
 Set custom thresholds for CPU and memory alerts
 
 Configure alert timeout periods
 
 Monitor processes exceeding resource thresholds

 
 # Contributing

1.Fork the repository

2.Create a feature branch

3.Commit your changes

4.Push to your branch

5.Create a Pull Request


# License

This project is licensed under the MITLicense. Feel free to use, modify, and distribute it as needed.
