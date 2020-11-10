import matplotlib.pyplot as plt
import scipy.stats as sps

top_100 = {'R': 37,
 'Python': 71,
 'SQL': 45,
 'C': 7,
 'Java': 17,
 'C++': 8,
 'Spark': 37,
 'Hadoop': 14,
 'C#': 1,
 'Tableau': 10,
 'Power BI': 11,
 'AWS': 19,
 'Azure': 21,
 'Scala': 29,
 'MATLAB': 3,
 'Pig': 1,
 'Hive': 7,
 'Impala': 2,
 'Teradata': 2,
 'Oracle': 3,
 'SAS': 9,
 'MongoDB': 2,
 'Redshift': 4,
 'S3': 3,
 'EC2': 2,
 'Lambda': 1,
 'EMR': 2,
 'SageMaker': 2,
 'DynamoDB': 3,
 'Cloudformation': 1,
 'Athena': 2,
 'Kinesis': 3,
 'Cassandra': 1,
 'Alteryx': 1,
 'Jupyter': 4,
 'Clickhouse': 1,
 'PyTorch': 2,
 'TensorFlow': 3}

top_all = {'R': 170,
 'Python': 435,
 'SQL': 467,
 'C': 54,
 'Java': 212,
 'C++': 54,
 'Spark': 129,
 'Hadoop': 77,
 'C#': 67,
 'Tableau': 116,
 'Power BI': 138,
 'AWS': 249,
 'Azure': 176,
 'Scala': 177,
 'MATLAB': 16,
 'Pig': 9,
 'Hive': 54,
 'Impala': 10,
 'Teradata': 20,
 'Oracle': 59,
 'SAS': 106,
 'MongoDB': 19,
 'Redshift': 48,
 'S3': 55,
 'EC2': 27,
 'Lambda': 34,
 'EMR': 28,
 'SageMaker': 6,
 'DynamoDB': 14,
 'Cloudformation': 8,
 'Athena': 24,
 'Kinesis': 12,
 'Cassandra': 15,
 'Alteryx': 17,
 'Jupyter': 14,
 'Clickhouse': 1,
 'PyTorch': 15,
 'TensorFlow': 19}

kw_freq = [(v,k) for k,v in top_100.items()]
kw_freq.sort(reverse=True)
for k,v in kw_freq:
    print(f"{k}: {v}")

plt.plot(sorted(top_100.values(), reverse=True))
plt.show()

kw_freq100 = [v for k,v in top_100.items() if v >= 5]
kw_freqall = [v for k,v in top_all.items() if top_100[k] >= 5]
chi = sps.chisquare(kw_freq100, f_exp=kw_freqall)
print(chi)