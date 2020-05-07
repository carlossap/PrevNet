from scapy.all import *

feat_file = open('features.txt','w')
label_file = open('labels.txt','w')

def ret_duration(pkts):
	#duration
	return pkts[-1].time - pkts[0].time

def ret_length(pkts):
	#number of packets
	pktsSize = 0
	for pkt in pkts:
		pktsSize=pktsSize + 1
	return pktsSize

def ret_total_size(pkts):
	#size of stream
	totalSize = 0
	for pkt in pkts:
		totalSize=totalSize+pkt.len
	return totalSize

def ret_sourcep(pkts):
	#malicious source port
	for p in pkts:
		return p.sport

def ret_destp(pkts):
	#malicious destination port
	for p in pkts:
		return p.dport

def ret_interval(pkts):
	#average time interval
	q_time = 0
	sum = 0
	count = 0
	for p in pkts:
		count = count + 1
		sum = sum + p.time - q_time
		q_time = p.time
	return (sum/count)

def ret_ttl(pkts):
	#time to live
	total_ttl = 0.0
	count = 0
	for p in pkts:
		count = count + 1
		total_ttl = total_ttl + p[IP].ttl
	return (total_ttl/count)

def ret_urgptr(pkts):
	# urgent pointer value
	urgptr = 0.0
	pkt_count = 0
	for p in pkts:
		pkt_count = pkt_count + 1
		urgptr = urgptr + p[TCP].urgptr
	return (urgptr/pkt_count)

for fname in os.listdir('benign/'):
  try:
	pkts = rdpcap('benign/'+str(fname))
	s = "%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f" % (ret_duration(pkts),ret_length(pkts),ret_total_size(pkts),ret_feature4(pkts),ret_feature5(pkts),ret_feature6(pkts),ret_feature7(pkts),ret_feature8(pkts))
	feat_file.write(s+"\n")
	label_file.write('0\n')
  except:
	print(str(fname))

for fname in os.listdir('malicious/'):
        pkts = rdpcap('malicious/'+str(fname))
        s = "%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f" % (ret_duration(pkts),ret_length(pkts),ret_total_size(pkts),ret_feature4(pkts),ret_feature5(pkts),ret_feature6(pkts),ret_feature7(pkts),ret_feature8(pkts))
        feat_file.write(s+"\n")
        label_file.write('1\n')

feat_file.close()
label_file.close()

#test
