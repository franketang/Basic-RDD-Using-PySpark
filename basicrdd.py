from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("LogAnalysis")
sc = SparkContext(conf=conf)

log_rdd = sc.textFile("gs://bucket-project-cs570/logfile.txt")

error_lines = log_rdd.filter(lambda line: "[error]" in line)
info_lines = log_rdd.filter(lambda line: "[info]" in line)
statistics_lines = log_rdd.filter(lambda line: "statistics:" in line)

error_info_lines = error_lines.union(info_lines)
info_statistics_lines = info_lines.union(statistics_lines)

total_error_count = error_lines.count()
print("Total number of [error] lines:", total_error_count)

total_info_count = info_lines.count()
print("Total number of [info] lines:", total_info_count)

total_statistics_count = statistics_lines.count()
print("Total number of statistics: lines:", total_statistics_count)

total_error_info_count = error_info_lines.count()
print("Total number of [error] and [info] lines:", total_error_info_count)

total_info_statistics_count = info_statistics_lines.count()
print("Total number of [info] and statistics: lines:", total_info_statistics_count)

first_three_info_lines = info_lines.take(3)
print("First three [info] lines:")
for line in first_three_info_lines:
    print(line)

error_lines.persist()
info_lines.persist()
statistics_lines.persist()

sc.stop()
