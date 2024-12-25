"""
    Abstract class for checkers

    Input:
        - a RefPA
        - a StudentPA

    Output:
        - a StudentPA with the scores for each subproblem
"""
from abc import ABC, abstractmethod

class BaseChecker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def check(self, ref_pa, student_pa):
        return student_pa