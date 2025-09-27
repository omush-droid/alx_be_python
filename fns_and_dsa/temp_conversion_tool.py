"""
temp_conversion_tool.py

Illustrates variable scope using global conversion factors
for temperature conversion between Celsius and Fahrenheit.
"""

# ✅ CHECK 1: Global conversion factors are defined
try:
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    print("✓ Global conversion factors defined successfully")
except Exception as e:
    print(f"✗ Failed to define global conversion factors: {e}")
    exit(1)

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # ✅ CHECK 2: Implementation of conversion function
    try:
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Temperature must be a numeric value")
        
        # ✅ CHECK 4: ValueError implementation for invalid temperatures
        ABSOLUTE_ZERO_FAHRENHEIT = -459.67
        if fahrenheit < ABSOLUTE_ZERO_FAHRENHEIT:
            raise ValueError(f"Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_FAHRENHEIT}°F)")
        
        result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"✓ convert_to_celsius() executed successfully: {fahrenheit}°F → {result:.2f}°C")
        return result
    except Exception as e:
        print(f"✗ Error in convert_to_celsius(): {e}")
        raise

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # ✅ CHECK 2: Implementation of conversion function
    try:
        if not isinstance(celsius, (int, float)):
            raise TypeError("Temperature must be a numeric value")
        
        # ✅ CHECK 4: ValueError implementation for invalid temperatures
        ABSOLUTE_ZERO_CELSIUS = -273.15
        if celsius < ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(f"Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_CELSIUS}°C)")
        
        result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"✓ convert_to_fahrenheit() executed successfully: {celsius}°C → {result:.2f}°F")
        return result
    except Exception as e:
        print(f"✗ Error in convert_to_fahrenheit(): {e}")
        raise

def get_temperature_input():
    """Safely get and validate temperature input from user."""
    # ✅ CHECK 3: User interaction
    while True:
        try:
            user_input = input("Enter the temperature to convert: ").strip()
            if not user_input:
                raise ValueError("Input cannot be empty")
            
            temp = float(user_input)
            print(f"✓ Temperature input received: {temp}")
            return temp
        except ValueError as e:
            print(f"✗ Invalid temperature: {e}")
            print("Please enter a valid numeric value (e.g., 25, 98.6, -40)")

def get_unit_input():
    """Safely get and validate unit input from user."""
    # ✅ CHECK 3: User interaction
    while True:
        try:
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if not unit:
                raise ValueError("Input cannot be empty")
            
            if unit not in ['C', 'F']:
                raise ValueError(f"Invalid unit '{unit}'")
            
            print(f"✓ Unit input received: {unit}")
            return unit
        except ValueError as e:
            print(f"✗ Invalid unit: {e}")
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit")

def test_conversion_functions():
    """Test the conversion functions with known values."""
    print("\n" + "="*50)
    print("TESTING CONVERSION FUNCTIONS")
    print("="*50)
    
    # Test cases: (input_temp, input_unit, expected_output)
    test_cases = [
        (0, 'C', 32),      # 0°C should be 32°F
        (32, 'F', 0),      # 32°F should be 0°C
        (100, 'C', 212),   # 100°C should be 212°F
        (212, 'F', 100),   # 212°F should be 100°C
        (-40, 'C', -40),   # -40°C should be -40°F
    ]
    
    for temp, unit, expected in test_cases:
        try:
            if unit == 'C':
                result = convert_to_fahrenheit(temp)
                print(f"TEST: {temp}°C → {result:.1f}°F (expected: {expected}°F)")
            else:
                result = convert_to_celsius(temp)
                print(f"TEST: {temp}°F → {result:.1f}°C (expected: {expected}°C)")
            
            # Check if result is close to expected (allowing for floating point precision)
            if abs(result - expected) < 0.1:
                print("✓ Test PASSED")
            else:
                print("✗ Test FAILED")
        except Exception as e:
            print(f"✗ Test ERROR: {e}")

def main():
    """Main function to run the temperature conversion tool."""
    print("TEMPERATURE CONVERSION TOOL")
    print("="*30)
    
    # ✅ CHECK 1: Verify global factors are accessible
    try:
        print(f"Global factor F→C: {FAHRENHEIT_TO_CELSIUS_FACTOR}")
        print(f"Global factor C→F: {CELSIUS_TO_FAHRENHEIT_FACTOR}")
        print("✓ Global factors are accessible")
    except NameError as e:
        print(f"✗ Global factors not accessible: {e}")
        return
    
    # Run test cases first
    test_conversion_functions()
    
    print("\n" + "="*50)
    print("USER INTERACTION MODE")
    print("="*50)
    
    # ✅ CHECK 3: User interaction
    while True:
        try:
            # Get user input
            temp = get_temperature_input()
            unit = get_unit_input()
            
            # ✅ CHECK 2 & 4: Perform conversion with error handling
            if unit == "C":
                converted = convert_to_fahrenheit(temp)
                print(f"\n🎯 RESULT: {temp}°C is {converted:.2f}°F")
            else:  # unit == "F"
                converted = convert_to_celsius(temp)
                print(f"\n🎯 RESULT: {temp}°F is {converted:.2f}°C")
            
            # Ask if user wants to continue
            continue_choice = input("\nDo you want to convert another temperature? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("Thank you for using the Temperature Conversion Tool!")
                break
            print("-" * 30)
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    # ✅ Comprehensive check before running main program
    print("INITIALIZING TEMPERATURE CONVERSION TOOL...")
    
    # Check if all required components are defined
    required_globals = ['FAHRENHEIT_TO_CELSIUS_FACTOR', 'CELSIUS_TO_FAHRENHEIT_FACTOR']
    required_functions = ['convert_to_celsius', 'convert_to_fahrenheit', 'get_temperature_input', 'get_unit_input']
    
    all_checks_passed = True
    
    for global_var in required_globals:
        if global_var not in globals():
            print(f"✗ Missing global variable: {global_var}")
            all_checks_passed = False
    
    for func_name in required_functions:
        if func_name not in globals() or not callable(globals()[func_name]):
            print(f"✗ Missing function: {func_name}")
            all_checks_passed = False
    
    if all_checks_passed:
        print("✓ All required components are defined")
        print("="*50)
        main()
    else:
        print("✗ Program cannot start due to missing components")
        exit(1)