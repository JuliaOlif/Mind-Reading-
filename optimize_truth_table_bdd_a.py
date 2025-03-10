#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from itertools import permutations
from pyeda.inter import bddvars, expr2bdd, expr

def parse_truth_table(lines):
    """
    Parses the truth table from input lines.
    Args:
        lines (list): List of strings representing the truth table.
    Returns:
        var_names (list): List of variable names.
        input_combinations (list): List of input combinations (rows of the 
                                                               truth table).
        outputs (list): List of output values corresponding to each input combination.
    """
    # Parse header to get variable names
    header = lines[0].strip('|').split('|')
    var_names = [col.strip() for col in header[:-2]]  # Exclude output column

    input_combinations = []
    outputs = []

