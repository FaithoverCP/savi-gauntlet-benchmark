#!/usr/bin/env python3
"""
SAVI Gauntlet - repeatability check
Copyright (c) 2025 Michael Urbanowicz / Tekstein Scientific Inc.
MIT License

Sends one arithmetic prompt to a Gemini model several times with greedy decoding
(temperature 0, top_k 1) and reports whether the answer is correct (386.7) and
whether the outputs are identical. The prompt contains no SAVI instructions, so
the result says nothing about what the SAVI Protocol contributes.
"""

import os
import sys
import time
from typing import List, Dict, Tuple
from datetime import datetime

try:
    import google.generativeai as genai
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)


# ============================================================================
# CONFIGURATION
# ============================================================================

# Load environment variables
load_dotenv()

# Gauntlet v3 Test Prompt
GAUNTLET_PROMPT = """
Calculate the following mathematical expression and return ONLY the numeric result:

((17 * 23) + (89 - 42)) / (13 + 7) * (31 - 18) + (101 * 2) - (67 + 33)

Return ONLY the numeric answer. No explanations. No formatting. Just the number.
"""

# Expected correct answer (for verification)
EXPECTED_ANSWER = "386.7"  # (391 + 47) / 20 * 13 + 202 - 100 = 21.9 * 13 + 102 = 386.7 (corrected 2026-10-28; was 385.05)

# Test parameters
NUM_RUNS = 5
MODEL_NAME = "gemini-2.0-flash-exp"

# Greedy decoding settings (standard Gemini parameters)
GENERATION_CONFIG = {
    "temperature": 0.0,  # Zero temperature for determinism
    "top_p": 1.0,
    "top_k": 1,
    "max_output_tokens": 50,  # Minimal output constraint
}


# ============================================================================
# SAVI PROTOCOL WRAPPER
# ============================================================================

def initialize_savi_model(api_key: str) -> genai.GenerativeModel:
    """
    Initialize the Gemini model with greedy decoding settings.
    
    Args:
        api_key: Google AI API key
        
    Returns:
        Configured GenerativeModel instance
    """
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config=GENERATION_CONFIG
    )
    
    return model


# ============================================================================
# TEST EXECUTION
# ============================================================================

def run_single_test(model: genai.GenerativeModel, run_number: int) -> Tuple[str, float]:
    """
    Execute a single Gauntlet test run.
    
    Args:
        model: Configured GenerativeModel
        run_number: Current run number (for logging)
        
    Returns:
        Tuple of (response_text, execution_time)
    """
    print(f"  Run {run_number}/{NUM_RUNS}...", end=" ", flush=True)
    
    start_time = time.time()
    response = model.generate_content(GAUNTLET_PROMPT)
    execution_time = time.time() - start_time
    
    result = response.text.strip()
    print(f"✓ ({execution_time:.3f}s)")
    
    return result, execution_time


def calculate_determinism_score(results: List[str]) -> float:
    """
    Calculate the determinism score (% of matching outputs).
    
    Args:
        results: List of output strings from multiple runs
        
    Returns:
        Determinism score as percentage (0-100)
    """
    if not results:
        return 0.0
    
    # Count occurrences of each unique output
    unique_outputs = {}
    for result in results:
        unique_outputs[result] = unique_outputs.get(result, 0) + 1
    
    # Find most common output
    max_matches = max(unique_outputs.values())
    
    # Calculate percentage
    score = (max_matches / len(results)) * 100
    
    return score


def verify_correctness(result: str) -> bool:
    """
    Verify if the result matches expected answer.
    
    Args:
        result: Model output
        
    Returns:
        True if correct, False otherwise
    """
    # Clean the result (remove whitespace, compare numeric value)
    cleaned_result = result.strip()
    
    # Try to extract just the number
    try:
        # Handle cases where model might add formatting
        import re
        numbers = re.findall(r'-?\d+\.?\d*', cleaned_result)
        if numbers:
            result_value = float(numbers[0])
            expected_value = float(EXPECTED_ANSWER)
            return abs(result_value - expected_value) < 0.01  # Allow small floating point error
    except:
        pass
    
    return cleaned_result == EXPECTED_ANSWER


# ============================================================================
# RESULTS ANALYSIS
# ============================================================================

def print_results(results: List[str], execution_times: List[float]):
    """
    Print comprehensive test results and analysis.
    
    Args:
        results: List of output strings
        execution_times: List of execution times
    """
    print("\n" + "="*80)
    print("GAUNTLET v3 TEST RESULTS")
    print("="*80)
    
    # Check correctness
    is_correct = verify_correctness(results[0]) if results else False
    correctness_status = "✅ CORRECT" if is_correct else "❌ INCORRECT"
    
    print(f"\n📊 CORRECTNESS: {correctness_status}")
    print(f"   Expected: {EXPECTED_ANSWER}")
    print(f"   Got:      {results[0] if results else 'N/A'}")
    
    # Calculate determinism
    determinism = calculate_determinism_score(results)
    determinism_status = "✅ DETERMINISTIC" if determinism == 100.0 else "⚠️  NON-DETERMINISTIC"
    
    print(f"\n🎯 DETERMINISM SCORE: {determinism:.1f}% {determinism_status}")
    
    # Show all outputs
    print(f"\n📋 ALL OUTPUTS ({NUM_RUNS} runs):")
    for i, result in enumerate(results, 1):
        print(f"   Run {i}: {result}")
    
    # Execution time stats
    avg_time = sum(execution_times) / len(execution_times)
    min_time = min(execution_times)
    max_time = max(execution_times)
    
    print(f"\n⏱️  EXECUTION TIME:")
    print(f"   Average: {avg_time:.3f}s")
    print(f"   Min:     {min_time:.3f}s")
    print(f"   Max:     {max_time:.3f}s")
    
    # Final verdict
    print("\n" + "="*80)
    if is_correct and determinism == 100.0:
        print("✅ RESULT: correct, and identical across all runs")
    elif is_correct:
        print(f"⚠️  RESULT: correct, but outputs varied across runs ({determinism:.1f}% identical)")
    else:
        print("❌ RESULT: incorrect answer")
    print("="*80 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function for SAVI Gauntlet Benchmark.
    """
    print("\n" + "="*80)
    print("SAVI GAUNTLET BENCHMARK v3.0")
    print("Repeatability check")
    print("="*80)
    print(f"\n📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🤖 Model:     {MODEL_NAME}")
    print(f"🔄 Runs:      {NUM_RUNS}")
    print(f"🌡️  Temp:      {GENERATION_CONFIG['temperature']}")
    
    # Get API key
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    if not api_key:
        print("\n❌ ERROR: GOOGLE_AI_API_KEY not found in environment variables")
        print("Please create a .env file with: GOOGLE_AI_API_KEY=your_key_here")
        sys.exit(1)
    
    # Initialize model
    print("\n🔧 Initializing model...")
    model = initialize_savi_model(api_key)
    print("✓ Model initialized with greedy decoding settings")
    
    # Run tests
    print(f"\n🚀 Executing {NUM_RUNS} test runs...")
    results = []
    execution_times = []
    
    for i in range(1, NUM_RUNS + 1):
        try:
            result, exec_time = run_single_test(model, i)
            results.append(result)
            execution_times.append(exec_time)
            time.sleep(0.5)  # Small delay between runs
        except Exception as e:
            print(f"❌ ERROR on run {i}: {str(e)}")
            sys.exit(1)
    
    # Print results
    print_results(results, execution_times)


if __name__ == "__main__":
    main()
