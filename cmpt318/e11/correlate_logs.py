#!/usr/bin/python3

# reddit_averages.py
# CMPT 318 Exercise 11 - Server Log Correlation
# Alex Macdonald
# ID#301272281
# November 24, 2017

import math
import sys
from pyspark.sql import SparkSession, functions, types, Row
import re

spark = SparkSession.builder.appName('correlate logs').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+

line_re = re.compile("^(\\S+) - - \\[\\S+ [+-]\\d+\\] \"[A-Z]+ \\S+ HTTP/\\d\\.\\d\" \\d+ (\\d+)$")


def line_to_row(line):
    """
    Take a logfile line and return a Row object with hostname and bytes transferred. Return None if regex doesn't match.
    """
    m = line_re.match(line)
    if m:
        row = Row(hostname=m.group(1), num_bytes=m.group(2))
        return row
    else:
        return None

def not_none(row):
    """
    Is this None? Hint: .filter() with it.
    """
    return row is not None


def create_row_rdd(in_directory):
    log_lines = spark.sparkContext.textFile(in_directory)
    log_lines = log_lines.map(line_to_row).filter(not_none)
    return log_lines # return an RDD of Row() objects

def calculate_correlation_coefficient(row):
    n = row[0]
    sig_xi = row[1]
    sig_xi2 = row[2]
    sig_yi = row[3]
    sig_yi2 = row[4]
    sig_xiyi = row[5]
    numerator = (n*sig_xiyi)-(sig_xi*sig_yi)
    denominator_left = math.sqrt((n*sig_xi2)-(sig_xi**2))
    denominator_right = math.sqrt((n*sig_yi2)-(sig_yi**2))
    denominator = denominator_left*denominator_right
    return numerator/denominator

def main():
    in_directory = sys.argv[1]
    create_row_rdd(in_directory)

    # 1. Get the data out of the files into a DataFrame where you have the hostname and # of bytes/request
    logs = spark.createDataFrame(create_row_rdd(in_directory)).cache()

    # 2. Group by hostname; get the number of requests and sum of bytes transferred, to form a data point
    sum_request_bytes = logs.groupby('hostname').agg(functions.sum('num_bytes').alias("sum_request_bytes")).cache()
    count_requests = logs.groupby('hostname').agg(functions.count('hostname').alias("count_requests")).cache()
    data = count_requests.join(sum_request_bytes, "hostname").cache()

    # 3. Produce six values, and add them to get the six sums
    # Idea to use lit(1) from StackOverFlow post at:
    # https://stackoverflow.com/questions/33681487/how-do-i-add-a-new-column-to-a-spark-dataframe-using-pyspark
    data = data.withColumn('1', functions.lit(1))
    data = data.withColumn('xi', data.count_requests)
    data = data.withColumn('xi^2', pow(data.count_requests, 2))  
    data = data.withColumn('yi', data.sum_request_bytes)
    data = data.withColumn('yi^2', pow(data.sum_request_bytes, 2))
    data = data.withColumn('xiyi', data.count_requests * data.sum_request_bytes)
    data = data.drop("sum_request_bytes", "count_requests")
    # Idea to use empty groupby courtesy of ggbaker in the exercise notes
    data = data.groupby().sum()

    # 4. Calculate the final value of r
    row = data.first()
    r = calculate_correlation_coefficient(row)

    print("r = %g\nr^2 = %g" % (r, r**2))


if __name__=='__main__':
    main()