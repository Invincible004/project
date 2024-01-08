def is_valid_move(current, move):
    # Check if the move is valid based on the puzzle rules
    return current[-1] != move

def generate_all_sequences(current, remaining_moves):
    if not remaining_moves:
        return [current]

    all_sequences = []
    for move in remaining_moves:
        if is_valid_move(current, move):
            new_sequence = current + [move]
            new_remaining_moves = remaining_moves.copy()
            new_remaining_moves.remove(move)
            all_sequences.extend(generate_all_sequences(new_sequence, new_remaining_moves))

    return all_sequences

def print_solution(solution):
    for i, move in enumerate(solution):
        print(f"Cube {i + 1}: {move}")

def main():
    # Define cube types: 'e' for end, 's' for straight, 'b' for bend
    cube_types = ['e', 's', 'b']

    # Generate all possible sequences
    all_sequences = generate_all_sequences(['e'], cube_types * 26)

    # Print all solutions
    for i, solution in enumerate(all_sequences):
        print(f"\nSolution {i + 1}:")
        print_solution(solution)

if __name__ == "__main__":
    main()
