#!/usr/bin/env python3

import numpy as np
from numpy import ndarray


STUDENT_NAME = 'Юрий Сыровецкий'
STUDENT_NUMBER = 8
VARIANT = 2 - STUDENT_NUMBER % 2


class Perceptron:
    activate = staticmethod(lambda s: 1 if s >= 0.5 else 0)
    x0: float = 1

    def __init__(self, learn_factor: float):
        self.learn_factor = learn_factor
        self.weights = np.random.uniform(-1, 1, size=3)
        self.err_sum = 0
        self.sample_count = 0

    def predict(self, input_extended: ndarray) -> float:
        return self.activate(np.dot(self.weights, input_extended))

    def learn(self, input: ndarray, target: float) -> float:
        input_extended = np.insert(input, 0, self.x0)
        output = self.predict(input_extended)
        err = target - output
        Δweights = self.learn_factor * err * input_extended
        self.weights += Δweights
        self.err_sum += err * err
        self.sample_count += 1

    def mean_square_error(self):
        return self.err_sum / 2 / self.sample_count


LEARN_FACTORS = [0.03, 0.2, 0.4, 0.6, 0.8, 0.95]


for learn_factor in LEARN_FACTORS:
    print('Эксперимент с коэффициентом обучения', learn_factor)
    perceptron = Perceptron(learn_factor)
    for epoch in range(20):
        perceptron.learn(np.array([0, 0]), 0)
        perceptron.learn(np.array([0, 1]), 0)
        perceptron.learn(np.array([1, 0]), 0)
        perceptron.learn(np.array([1, 1]), 1)
        print(
            '{}: {:.2}'.format(epoch, perceptron.mean_square_error()),
            end=', '
        )
    print()