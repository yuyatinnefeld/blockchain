import collections
import hashlib

def create_hash(value):
    hased_v = hashlib.sha256(value.encode()).hexdigest()
    return hased_v


def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(
        sorted(unsorted_dict.items(), key=lambda d:d[0]))


# print("="*20, "unsorted original block", "="*20)
# block1 = {'b': 2, 'a': 1}
# block2 = {'a': 1, 'b': 2}
# print(create_hash(str(block1)))
# print(create_hash(str(block2)))


# print("="*20, "key val paar sorted block", "="*20)
# block_1 = sorted_dict_by_key(block1)
# block_2 = sorted_dict_by_key(block2)
# print(create_hash(str(block_1)))
# print(create_hash(str(block_2)))
