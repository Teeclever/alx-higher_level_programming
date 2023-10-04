#!/usr/bin/python3
"""Defines a matrix multiplication function using the NumPy. library"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): First matrix.
        m_b (list of lists of ints/floats): Second matrix.
    """

    return np.matmul(m_a, m_b)
