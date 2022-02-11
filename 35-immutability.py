# Immutability

selfish = '01234567'
        #  01234567

selfish[0] = '8' # this can't be done becasue thew strings are immutable
selfish = '8' # we need to reasign the value
print(selfish)