import random
from math import log

def get_free_channel_idx(K):
    idx = 0
    for channel in K:
        if (channel.t_begin == None) and (channel.t_end == None):
            return idx
        idx += 1

    return -1

class event:


    def __init__(self, id):
        self.id = id
        self.t_in = None
        self.t_begin = None
        self.t_end = None
        self.type_of = None
        self.channel_id = None

    def save_event(self, begin, end, channel_id):
        self.t_begin = begin
        self.t_end = end

        self.channel_id = channel_id


class channel:


    def __init__(self, id):
        self.id = id
        self.t_begin = None  # if is free
        self.t_end = None  # if is free
        self.type_of = None
        self.event_id = None

    def save_channel(self, begin, end, event_id):
        self.t_begin = begin
        self.t_end = end

        self.event_id = event_id


lambda0 = 60
s = 50
k = 2
t = [-1/lambda0*log(random.random()) for i in range(s)]
S = [event(i) for i in range(s)]
for i in range(s):
    sum = 0
    for j in range(s):
        sum += t[j]
    S[i].t_in = sum

T_obsl = s

K = [channel(i) for i in range(k) ]



def get_channel_by_end_time(K, T):

    for idx in range(len(K)):
        if K[idx].t_end == T:
            return idx
        idx += 1








i, j = 0, 0
T = S[i].t_in
while T < T_obsl:
    if T == S[i].t_in :
        if get_free_channel_idx(K) != -1:
            diff = 4  # or generate
            j = get_free_channel_idx(K)
            S[i].save_event(T, T + diff, K[j].id)
            K[j].save_channel(T, T + diff, S[i].id)
            i += 1
            channels_end = [item.t_end for item in K]
            T = min(channels_end, S[i].t_in)
        else:  # add new channel
            diff = 4  # or generate
            K.append(channel(len(K)))
            K[-1].save_channel(T, T + diff, S[i].id)
            S[i].save_event(T, T + diff, K[j].id)

            i += 1
            channels_end = [item.t_end for item in K]
            T = min(channels_end, S[i].t_in)

    else:


        diff = 4  # or generate
        j = get_channel_by_end_time(K, T)
        if S[i].t_in < K[j].t_end:
            S[i].save_event(T, T + diff, K[j].id)
            K[j].save_channel(T, T + diff, S[i].id)
            i += 1
        channels_end = [item.t_end for item in K]
        T = min(channels_end, S[i].t_in)












