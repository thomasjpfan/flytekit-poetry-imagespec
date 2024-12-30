from flytekit import task, ImageSpec
import numpy as np
from random import choice
from string import ascii_letters


image = ImageSpec(
    name="numpy-poetry",
    requirements="poetry.lock",
    registry="localhost:30000",
    env={"A": "".join(choice(ascii_letters) for _ in range(20))},
)


@task(container_image=image)
def add_task() -> np.ndarray:
    x = np.ones(10)
    return x + 10
