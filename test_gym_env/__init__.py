from gym.envs.registration import register

register(
    id='test_gym_env-v0',
    entry_point='test_gym_env.envs:FooEnv',
)