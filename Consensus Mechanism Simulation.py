import random
def simulate_pow(validators):
    print("🔧 Proof of Work (PoW) Simulation")
    for miner, stats in validators.items():
        print(f"  {miner} -> power: {stats['power']}")
    selected = max(validators, key=lambda x: validators[x]['power'])
    print(f"Selected Validator (PoW): {selected} (highest computational power)\n")
    return selected
def simulate_pos(validators):
    print("🔧 Proof of Stake (PoS) Simulation")
    for staker, stats in validators.items():
        print(f"  {staker} -> stake: {stats['stake']}")
    selected = max(validators, key=lambda x: validators[x]['stake'])
    print(f"Selected Validator (PoS): {selected} (highest stake in network)\n")
    return selected
def simulate_dpos(validators, votes):
    print("🔧 Delegated Proof of Stake (DPoS) Simulation")
    print(f"  Voters: {votes}")
    vote_count = {v: votes.count(v) for v in validators}
    for delegate, count in vote_count.items():
        print(f"  {delegate} received {count} votes")
    max_votes = max(vote_count.values())
    top_candidates = [v for v, c in vote_count.items() if c == max_votes]
    selected = random.choice(top_candidates)
    print(f"Selected Validator (DPoS): {selected} (elected delegate by voting)\n")
    return selected
validators = {
    'Alice': {'power': random.randint(1, 100), 'stake': random.randint(100, 1000)},
    'Bob':   {'power': random.randint(1, 100), 'stake': random.randint(100, 1000)},
    'Carol': {'power': random.randint(1, 100), 'stake': random.randint(100, 1000)}
}

# Voters vote for one of the validators
voters = [random.choice(list(validators.keys())) for _ in range(3)]
pow_validator = simulate_pow(validators)
pos_validator = simulate_pos(validators)
dpos_validator = simulate_dpos(validators, voters)
