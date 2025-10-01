#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # compute means for numeric fields
    avg_heart_rate = float(data['heart_rate'].mean())
    avg_systolic_bp = float(data['blood_pressure_systolic'].mean())
    avg_glucose = float(data['glucose_level'].mean())

    return {
        'avg_heart_rate': avg_heart_rate,
        'avg_systolic_bp': avg_systolic_bp,
        'avg_glucose': avg_glucose,
    }


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    high_hr_count = (data['heart_rate'] > 90).sum()
    high_bp_count = (data['blood_pressure_systolic'] > 130).sum()
    high_glucose_count = (data['glucose_level'] > 110).sum()

    return {
        'high_heart_rate': high_hr_count,
        'high_blood_pressure': high_bp_count,
        'high_glucose': high_glucose_count,
    }


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    report = []
    report.append('Health Sensor Data Analysis Report')
    report.append('==================================')
    report.append('')
    report.append('Dataset Summary:')
    report.append(f'- Total readings: {total_readings}')
    report.append('')
    report.append('Average Measurements:')
    report.append(f"Heart Rate: {stats['avg_heart_rate']:.1f} bpm")
    report.append(f"Systolic BP: {stats['avg_systolic_bp']:.1f} mmHg")
    report.append(f"Glucose Level: {stats['avg_glucose']:.1f} mg/dL")
    report.append('')
    report.append('Abnormal Readings:')
    report.append(f"High Heart Rate (>90): {abnormal['high_heart_rate']} readings")
    report.append(f"High Blood Pressure (>130): {abnormal['high_blood_pressure']} readings")
    report.append(f"High Glucose (>110): {abnormal['high_glucose']} readings")
    report.append('')

    return '\n'.join(report)


def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # ensure parent directory exists
    import os
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)


def main():
    """Main execution function."""
    filename = 'health_data.csv'
    data = load_data(filename)

    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)

    report = generate_report(stats, abnormal, total_readings)

    out_file = 'output/analysis_report.txt'
    save_report(report, out_file)
    print(f'Analysis complete. Report saved to {out_file}')


if __name__ == "__main__":
    main()