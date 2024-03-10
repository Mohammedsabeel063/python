#!/bin/bash

# Function to calculate simple interest
calculate_simple_interest() {
    principal=$1
    rate=$2
    time=$3

    # Formula for simple interest: SI = P * R * T / 100
    interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)

    echo "Simple Interest: $interest"
}

# Main script
echo "Simple Interest Calculator"

# Input principal amount
read -p "Enter principal amount: " principal

# Input rate of interest
read -p "Enter rate of interest (in percentage): " rate

# Input time period
read -p "Enter time period (in years): " time

# Call function to calculate simple interest
calculate_simple_interest $principal $rate $time
