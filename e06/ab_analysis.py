#!/usr/bin/python3

# ab_analysis.py
# CMPT 318 Exercise 6 - A/B Testing
# Alex Macdonald
# ID#301272281
# October 20, 2017

import sys
import numpy as np
import pandas as pd
from scipy import stats

OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value: {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value: {more_searches_p:.3g}\n'
    '"Did more/less instructors use the search feature?" p-value: {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value: {more_instr_searches_p:.3g}'
)

def main():
    # Takes an input file on the command line ...
    searchdata_file = sys.argv[1]

    # And analyses the provided data to get p-values
    searchdata = pd.read_json(searchdata_file, orient='records', lines=True);

    # Users with an odd-numbered uid were shown a new-and-improved searchbox
    odd_uid = searchdata[searchdata['uid'] % 2 != 0]

    # Others [even-numbered] were shown the original design
    even_uid = searchdata[searchdata['uid'] % 2 == 0]
    
    # We're going to be using nonparametric tests:
    # In Contingency Table, categories will be:
    # uid even uid/odd uid ..
    # "searched at least once"/"never searched"
    # So this creates a table thats ..
    #                 [odd]                 [even]
    # [searched]      [odd && searched]     [even && searched]
    # [not searched]  [odd && not searched] [even && not searched]
    all_odd_searched = odd_uid[odd_uid['search_count'] > 0]['uid'].count()
    all_odd_not_searched = odd_uid[odd_uid['search_count'] == 0]['uid'].count()

    all_even_searched = even_uid[even_uid['search_count'] > 0]['uid'].count()
    all_even_not_searched = even_uid[even_uid['search_count'] == 0]['uid'].count()

    # Create a Contingency Table represented as a np.array 2D matrix
    all_contingency = np.array([
      [all_odd_searched, all_even_searched],
      [all_odd_not_searched, all_even_not_searched]
    ])

    # Did more users use the search feature? Did a different fraction of users have search count > 0?
    _, all_contingency_p, _, _ = stats.chi2_contingency(all_contingency)
    
    # Did users search more often? Is the number of searches per user different? Mann-Whitney
    _, all_mannwhitney_p = stats.mannwhitneyu(odd_uid['search_count'], even_uid['search_count'])

    # Now, repeat the above but only using instructor data
    inst_odd = odd_uid[odd_uid['is_instructor']]
    inst_even = even_uid[even_uid['is_instructor']]
    inst_odd_searched = inst_odd[inst_odd['search_count'] > 0]['uid'].count()
    inst_odd_not_searched = inst_odd[inst_odd['search_count'] == 0]['uid'].count()
    inst_even_searched = inst_even[inst_even['search_count'] > 0]['uid'].count()
    inst_even_not_searched = inst_even[inst_even['search_count'] == 0]['uid'].count()
    inst_contingency = np.array([
      [inst_odd_searched, inst_even_searched],
      [inst_odd_not_searched, inst_even_not_searched]
    ])
    _, inst_contingency_p, _, _ = stats.chi2_contingency(inst_contingency)
    _, inst_mannwhitney_p = stats.mannwhitneyu(inst_odd['search_count'], inst_even['search_count'])

    # Output
    print(OUTPUT_TEMPLATE.format(
        more_users_p=all_contingency_p,
        more_searches_p=all_mannwhitney_p,
        more_instr_p=inst_contingency_p,
        more_instr_searches_p=inst_mannwhitney_p,
    ))


if __name__ == '__main__':
    main()