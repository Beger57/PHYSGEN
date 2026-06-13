import numpy as np

G = 1.0
EPS = 0.1
DT = 0.01

N_BODIES = 5
STEPS = 200
N_SAMPLES = 1000


def compute_accelerations(pos, mass):
    n = len(pos)
    acc = np.zeros_like(pos)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            dx = pos[j] - pos[i]
            dist = np.sqrt((dx**2).sum() + EPS**2)

            force = G * mass[i] * mass[j] / (dist**3)
            acc[i] += force * dx / mass[i]

    return acc


def simulate():
    trajectories = []

    for _ in range(N_SAMPLES):
        pos = np.random.randn(N_BODIES, 2)
        vel = np.random.randn(N_BODIES, 2)
        mass = np.random.uniform(1, 10, (N_BODIES, 1))

        traj = []

        for _ in range(STEPS):
            acc = compute_accelerations(pos, mass)

            vel = vel + acc * DT
            pos = pos + vel * DT

            state = np.concatenate([pos, vel, mass], axis=1)
            traj.append(state)

        trajectories.append(np.stack(traj))

    trajectories = np.stack(trajectories)
    np.save("data/nbody_v1.npy", trajectories)

    print("Saved:", trajectories.shape)


if __name__ == "__main__":
    simulate()

