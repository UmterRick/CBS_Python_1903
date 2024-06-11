def concat_sequence_v1(s_1, s_2):
    for elem in s_1:
        yield elem
    for elem in s_2:
        yield elem


def concat_sequence_v2(s_1, s_2):
    yield from s_1
    yield from s_2


seq_1 = range(10)
seq_2 = range(10, 21)

result = concat_sequence_v1(seq_1, seq_2)
print(list(result))

result = concat_sequence_v2(seq_1, seq_2)
print(list(result))