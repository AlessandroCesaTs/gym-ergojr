from setuptools import setup

setup(
    name='gym_ergojr',
    version='1.3',
    install_requires=[
        'gymnasium', 'pybullet>=1.9.4', 'scikit-learn', 'scipy', "tqdm",
        "matplotlib", "numpy"
    ],
    include_package_data=True,
    package_data={'gym_ergojr':['scenes/*.xml','scenes/*mtl','scenes/*obj','scenes/*png','scenes/*gif']},
    )
