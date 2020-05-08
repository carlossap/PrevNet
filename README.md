# Anomaly Based Intrusion Detection - CSE 3810
Carlos Aguilar and Tony Godez

# Overview
  Throughout the semester, we covered several topics with information security.
For this lab, students were tasked with producing a tool based on one of the course
topics and demonstrating mastery on that same topic. This tool shall solve an aspect of
the difficult problem of cyber defense. The tool we have developed covers and reports
on the topic of “Network Intrusion Detection” using PCAP files.

# Background
  Network traffic captures are an amazing way to detect and prevent network
intrusions. The increase of usage and dependency of the internet around the globe over
the last couple of decades has led to the inevitable increase of potential threats for its
users. The recent COVID-19 pandemic has reminded us that more than ever we
depend on the internet to make our lives easier. Unfortunately, this involves the
exponential likeliness of an intruder in our networks. The increase of the usage of
applications like Zoom and Netflix lead us to believe that the increase of malware found
in tampered installation software is more dangerous than ever.
  The purpose of this project is to ease the detection and understanding of the
intrusions that may happen within a network. Godezilar is a python script that helps the
user by reading PCAPs and providing a report on them. A PCAP is an application
programming interface (API) that captures the packets in a network traffic. PCAPs can
be used as protocol analyzers, traffic generators, etc. For our purposes, the script reads
a chosen PCAP to detect network intrusion as it contains packets that may help us
identify potential malicious activity.
  An anomaly-based IDS can be used in most situations to detect unwanted
intrusion. The concept of its usage remains the same but implementations can vary
widely as there are different methods of attacking different systems and programs. Our
IDS allows the user to detect malicious network traffic that does not have a well-known
signature. That being said, a cleverly designed anomaly-based IDS can prevent newly
developed methods of malicious intrusion.

# How does it work?
  The script generates the report by extracting and analyzing the following features
of the PCAP:
1. TIme interval between packets
2. Time-to-live
3. Urgent pointer value
4. Duration
5. Number of packets
6. Total size of stream
7. Suspicious source port
8. Suspicious destination port

These features are analyzed through “sklearn” which uses a test set of benign
traffic to establish a baseline to detect anomalous behavior. Since this is a
behavior-based analysis, it is very adaptable to different test sets. In the sample we
used, including more features to observe decreased the accuracy and recall as a result
of potentially overfitting the data. However, we felt this was necessary given our original
model was very susceptible to underfitting with different types of network traffic.
  In conclusion, the report prints what the script classifies as malicious or benign
packets from the PCAP to ease the identification of the network traffic. At the end of the
day, the script simply helps the user identify what could be an indication for intrusion
traffic and implies that the user knows what contents should be generally contained as
the traffic will vary greatly from network to network depending on the tasks given to it
(i.e. streaming, local server, ftp server, etc.).

# Download
For execution, simply configure Godezilar by changing the PCAP features to be
read and the desired text file to save the report on. A test model must then be run to
provide the results. Godezilar will continue to be updated as newer and better ways to
detect intrusion traffic develop, and as more research is done on new ways
anomaly-based IDS’s are being compromised. A GUI, that is also planned for the future,
would be beneficial to users who would like additional control and a more in depth
analysis on their network traffic.
Note: (Repository name will change once we have decided the final name for the script).
