# Immutability

selfish = '01234567'
        #  01234567

selfish[0] = '8' # this can't be done because thew strings are immutable
selfish = '8' # we need to reassign the value
print(selfish)