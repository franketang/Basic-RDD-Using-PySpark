# Basic-RDD-Using-PySpark

# Log File Analysis with PySpark RDD Project on GCP

This project provides a framework to analyze and visualize log files using PySpark on Google Cloud Platform (GCP). It's aimed to help in understanding log file metrics, identifying trends, and extracting insights efficiently.


## Features:
- **Detailed Log Analysis**: Delve deep into your logs.
    - Display counts for different log levels like "[error]", "[info]", and "statistics:".
    - View the first 3 entries of "[info]" log lines.
    - Extended metrics for combined log levels.
- **Scalability**: Utilizes PySpark's capabilities to handle large datasets efficiently.
- **Google Cloud Integration**: Works cohesively with GCP for robust processing.

## Dependencies:
- **pyspark**: This project uses Spark's Python API.
- **Google Cloud SDK**: Required to access and manage Google Cloud resources.

## Getting Started:

1. **Clone & Setup**:
    - `git clone [repository-url]`
    - Navigate to the project directory and install dependencies.
    - Ensure the Google Cloud SDK is properly configured with the right permissions.

2. **Run the Analysis**:
    - Execute `python main.py`.
    - Observe the console for results.

3. **Review the Results**:
    - Go through the metrics derived from the log file. Further details can be found in the output section.

## Sample Output:
```bash
Total [error] lines: XX
Total [info] lines: YY
Total statistics: lines: ZZ
Combined [error] and [info] lines: WW
Combined [info] and statistics: lines: TT

First 3 [info] lines:
1. [info] ...
2. [info] ...
3. [info] ...
```

## Final Output:
 Total number of [error] lines: 2
Total number of [info] lines: 61
Total number of statistics: lines: 2
Total number of [error] and [info] lines:63
Total number of [info] and statistics:lines:63

<img width="1440" alt="Basic RDD using PySpark Output" src="https://github.com/franketang/Basic-RDD-Using-PySpark/assets/29631514/f060520b-3351-4444-8d3e-0ed20b0f9949">


## Project Roadmap:
- **Advanced Metrics**: Plans to support more log levels and unique patterns.
- **Temporal Analysis**: Aiming to provide hourly or daily breakdowns of logs.
- **Visualization**: Future integrations with visualization tools for better insights.

## Contribution:
This being a student project, feedback, code enhancements, suggestions, or bug reports are always appreciated. Feel free to fork the repo and make your contributions.

## License:
This project is under the MIT License. It's open for modifications and improvements.
