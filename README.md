# PE-Header-Analysis-for-Malware-Detection-Quarantine-and-Removal
This is a machine learning-based malware detection system designed to protect your computer from malicious software threats. It uses cutting-edge techniques to analyze Portable Executable (PE) files, detect potential malware, and offers users the ability to quarantine or remove threats.

In today's digital landscape, the internet's pervasive expansion has propelled malware into a major cyber threat, with far-reaching consequences. Malware, a broad term encompassing software designed to compromise system integrity, confidential data, and more, poses an ever-growing danger to individuals, organizations, and even governments. As the threat landscape evolves, so do the techniques employed by malicious actors to circumvent traditional antivirus defenses.

Our project, known as the "Static PE Header Malware Scanner," addresses the pressing need for advanced malware detection mechanisms. It focuses on the static analysis of Portable Executable (PE) file headers, a fundamental component of executable files in Windows systems. By scrutinizing these PE headers, we seek to identify signs of malicious intent and enhance overall cybersecurity.

<br>

## Objective

The primary objective of our project is to develop a reliable, efficient, and user-friendly malware detection system using PE header analysis. Specifically, we aim to:
1. Implement machine learning algorithms for classifying PE files into malicious and legitimate categories based on their header attributes.
2. Provide the option to quarantine or remove identified malware, thus enhancing cybersecurity efforts.
3. Create a command-line interface for user interaction and real-time scanning of files.
4. Develop a straightforward setup process for ease of use.

our project's overarching objective is to provide a valuable contribution to the realm of cybersecurity. By employing advanced techniques for analyzing PE file headers, our system aims to elevate digital safety and equip users with a powerful tool to combat the ever-evolving landscape of malware threats. Through machine learning, user-friendly interfaces, and proactive threat management, we endeavor to provide a comprehensive solution that bolsters overall cybersecurity and safeguards against potential threats.

<br>

## Dataset

https://www.kaggle.com/datasets/dscclass/malware/data

<br>

## Files

#### Python Scripts

main.py
PE_main.py
quarantine_or_remove.py

#### Dataset

data.csv

#### Classifier

classifier.pkl
features.pkl
pickle_model.pkl
pickle_vector.pkl

<br>

## Project Requirements

joblib==1.1.0
numpy==1.24.3
pandas==2.0.1
pyfiglet==0.8.post1
python-dateutil==2.8.2
pytz==2023.3
scikit-learn==0.24.1
scipy==1.10.1
six==1.16.0
threadpoolctl==3.1.0
tzdata==2023.3

<br>

## System Architecture

![IW2 drawio](https://github.com/MMJ02/PE-Header-Analysis-for-Malware-Detection-Quarantine-and-Removal/assets/60285174/58c63c22-909f-41d8-98da-b2ea7839de8d)

<br>

## UI with Tests and Results

<img width="643" alt="1" src="https://github.com/MMJ02/PE-Header-Analysis-for-Malware-Detection-Quarantine-and-Removal/assets/60285174/030618f6-fd5f-4133-bffc-1253894c597b">


<img width="651" alt="2" src="https://github.com/MMJ02/PE-Header-Analysis-for-Malware-Detection-Quarantine-and-Removal/assets/60285174/ed85fd78-ad0d-48a9-baa1-6edd2045211a">


<img width="460" alt="4" src="https://github.com/MMJ02/PE-Header-Analysis-for-Malware-Detection-Quarantine-and-Removal/assets/60285174/85fb3c4d-cb3e-4c3e-a2a9-0e25fe087931">


<br><br><br>


## Did you know? 

The first computer virus, known as the "Creeper," was created in the early 1970s as an experiment rather than for malicious purposes. It simply displayed the message "I'm the creeper, catch me if you can!" on infected computers. Since then, the world of malware has evolved significantly, emphasizing the importance of robust malware detection tools like the one presented in this project.


