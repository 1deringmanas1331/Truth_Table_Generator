# 
import itertools
# Checks which gate is asked by the user
def logic_gate(inputs, gate_type):
    if gate_type == "AND":
        return all(inputs)
    elif gate_type == "OR":
        return any(inputs)
    elif gate_type == "XOR":
        return sum(inputs) % 2 == 1
    elif gate_type == "NOT":
        return not inputs[0]
    else:
        raise ValueError("Invalid gate type")


def generate_truth_table(inputs_count, gate_type):
    
    
    input_combinations = list(itertools.product([0, 1], repeat=inputs_count))
    
    header = " | ".join([f"I{i}" for i in range(1, inputs_count + 1)] + ["Output"])
    print(f"Truth table for {gate_type} gate with {inputs_count} inputs:")
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    for inputs in input_combinations:
        output = logic_gate(inputs, gate_type)
        input_str = " | ".join(map(str, inputs))
        print(f"{input_str} | {output} |")

gate_type = input("Enter the gate type (AND, OR, XOR, NOT): ").upper()
inputs_count = int(input("Enter the number of inputs (2 or 3): "))

if inputs_count < 2 or inputs_count > 3:
    print("Invalid number of inputs. Please choose 2 or 3.")
else:
    generate_truth_table(inputs_count, gate_type)
