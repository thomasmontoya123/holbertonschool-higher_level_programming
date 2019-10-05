#!/usr/bin/python3
"""Lazy matrix multiplication module

"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """function that two matrices.

            Parameters
            ----------
            m_a : list of list
                matrix a

            m_b : list of list
                matrix b

        """
    try:
        return [numpy.matmul(m_a, m_b)]
    except:
        raise
