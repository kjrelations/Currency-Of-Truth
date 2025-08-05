# DNA Seeding Simulation - Conceptual Prototype
# Simulate how encoded data in plant seed DNA mutates across generations,
# becoming individually unreadable but collectively recoverable

import random
import string
import hashlib
import matplotlib.pyplot as plt

# Helper function to simulate DNA encoding of a message
def encode_to_dna(message):
    binary = ''.join(format(ord(c), '08b') for c in message)
    return binary.replace('00', 'A').replace('01', 'C').replace('10', 'G').replace('11', 'T')

# Helper function to simulate mutation

def mutate_dna(dna, mutation_rate=0.01):
    bases = ['A', 'C', 'G', 'T']
    mutated = []
    for base in dna:
        if random.random() < mutation_rate:
            mutated.append(random.choice([b for b in bases if b != base]))
        else:
            mutated.append(base)
    return ''.join(mutated)

# Helper function to simulate decoding (naively)
def decode_dna(dna):
    binary = dna.replace('A', '00').replace('C', '01').replace('G', '10').replace('T', '11')
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)

# Generate a population of seeds with DNA
def simulate_generations(message, generations=5, seeds_per_generation=50, mutation_rate=0.01):
    original_dna = encode_to_dna(message)
    population = [original_dna for _ in range(seeds_per_generation)]
    
    all_generations = [population]
    for g in range(generations):
        new_population = [mutate_dna(seed, mutation_rate) for seed in population]
        all_generations.append(new_population)
        population = new_population

    return all_generations

# Attempt to recover message by majority base selection
def recover_message(dna_population):
    sequence_length = len(dna_population[0])
    recovered_dna = ''
    for i in range(sequence_length):
        bases_at_i = [dna[i] for dna in dna_population]
        majority_base = max(set(bases_at_i), key=bases_at_i.count)
        recovered_dna += majority_base
    return decode_dna(recovered_dna)

# Main execution
if __name__ == '__main__':
    message = "The currency of truth is meaning"
    generations = simulate_generations(message, generations=10, seeds_per_generation=100, mutation_rate=0.02)

    # Plot mutation effect
    diffs = []
    for g, pop in enumerate(generations):
        avg_diff = sum([sum([c1 != c2 for c1, c2 in zip(seed, generations[0][0])]) for seed in pop]) / len(pop)
        diffs.append(avg_diff)

    plt.plot(diffs)
    plt.title("Average DNA Mutation Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Avg. Mutated Bases")
    plt.show()

    # Try to recover message from last generation
    recovered = recover_message(generations[-1])
    print("Original message:", message)
    print("Recovered message:", recovered)