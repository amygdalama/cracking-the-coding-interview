import itertools

def num_hits(guess, solution):
    hit_count = 0
    pseudo_hit_count = 0
    guess_pool = guess[:]
    solution_pool = solution[:]
    for guess_slot, solution_slot in itertools.izip(guess, solution):
        if guess_slot == solution_slot:
            hit_count += 1
            guess_pool.remove(guess_slot)
            solution_pool.remove(solution_slot)
    for guess_slot in guess_pool:
        if guess_slot in solution_pool:
            pseudo_hit_count += 1
            solution_pool.remove(guess_slot)
    return hit_count, pseudo_hit_count

if __name__ == '__main__':
    assert num_hits(list('GGRR'), list('RGBY')) == (1, 1)

