from __future__ import print_function
import numpy as np

def gen_ids(shape, idx, ids):
    if idx >= len(shape):
        return ids
    next_ids = []
    for prev_id in ids:
        for n in range(shape[idx]):
            next_id = prev_id + [n]
            next_ids.append(next_id)
    return gen_ids(shape, idx + 1, next_ids)

def gen_ids_iter(shape):
    ids = [[]]
    for i in range(len(shape)):
        next_ids = []
        for prev_id in ids:
            for n in range(shape[i]):
                next_ids.append(prev_id + [n])
        ids = next_ids
    return ids

def transpose(a, dim_a, dim_b):
    assert dim_a != dim_b
    assert dim_a >= 0 and dim_a < len(a.shape)
    assert dim_b >= 0 and dim_b < len(a.shape)
    ids = gen_ids_iter(a.shape)
    ret_shape = list(a.shape)
    ret_shape[dim_a] = a.shape[dim_b]
    ret_shape[dim_b] = a.shape[dim_a]
    ret = np.empty(ret_shape)
    for idx in ids:
        trans_idx = list(idx)
        trans_idx[dim_a] = idx[dim_b]
        trans_idx[dim_b] = idx[dim_a]
        aa = a.item(tuple(idx))
        ret.itemset(tuple(trans_idx), aa)
    return ret

# TODO implement reshape

a = np.random.randint(2, size=(2, 2, 3))
print("a")
print(a)
trans_a = transpose(a, 0, 1)
print("trans_a")
print(trans_a)
print("transpose")
print(np.transpose(a, (1, 0, 2)))
