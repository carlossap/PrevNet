from scapy.all import *

feat_file = open('features.txt','w')
label_file = open('labels.txt','w')

def ret_duration(pkts):
	return pkts[-1].time - pkts[0].time

def ret_feature2(pkts):
	pktsSize = 0
	for pkt in pkts:
		pktsSize=pktsSize + 1
	return pktsSize
	#return 2

def ret_feature3(pkts):
	totalSize = 0
	for pkt in pkts:
		totalSize=totalSize+pkt.len
	return totalSize
	#return 3

def ret_feature4(pkts):
	for p in pkts:
		if p.sport != 443:
			return p.sport
	#return 4

def ret_feature5(pkts):
	for p in pkts:
		if p.dport != 443:
			return p.dport
	#return 5

for fname in os.listdir('benign/'):
  try:
	pkts = rdpcap('benign/'+str(fname))
	s = "%.5f,%.5f,%.5f,%.5f,%.5f" % (ret_duration(pkts),ret_feature2(pkts),ret_feature3(pkts),ret_feature4(pkts),ret_feature5(pkts))
	feat_file.write(s+"\n")
	label_file.write('0\n')
  except:
	print(str(fname))

for fname in os.listdir('malicious/'):
        pkts = rdpcap('malicious/'+str(fname))
        s = "%.5f,%.5f,%.5f,%.5f,%.5f" % (ret_duration(pkts),ret_feature2(pkts),ret_feature3(pkts),ret_feature4(pkts),ret_feature5(pkts))
        feat_file.write(s+"\n")
        label_file.write('1\n')

feat_file.close()
label_file.close()

#test
