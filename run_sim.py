import numpy as np
import matplotlib.pyplot as plt
from flybody.fly_envs import walk_imitation

print("1. Loading fruit fly physics environment...")
env = walk_imitation()
env.reset()

print("2. Simulating 50 steps of joint movements...")
for _ in range(50):
    action = np.random.normal(size=59)
    env.step(action)

print("3. Rendering fly camera view via virtual display...")
frame = env.physics.render(camera_id=0, height=480, width=640)

# Save the rendered frame as an image
plt.imsave("fruit_fly_simulation.png", frame)
print("SUCCESS: Simulation complete! Generated 'fruit_fly_simulation.png'")
