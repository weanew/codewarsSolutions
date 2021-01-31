def order_weight(strng):
    if strng == "":
        return ""
    nums = strng.split(' ')
    weights = []
    for i in range(0, len(nums)):
        weight = 0
        for ch in nums[i]:
            weight += int(ch)
        weights.append((weight, i))
    weights.sort(key=lambda x: x[0])
    for i in range(0, len(weights)):
        indexes = []
        for  j in range(0, len(weights)):
            if weights[i][0] == weights[j][0]:
                indexes.append(j)
        
        if len(indexes) > 1:
            elems = [weights[i] for i in indexes]
            elems.sort(key=lambda x: nums[x[1]])
            
            index = 0
            for j in range(0, len(indexes)):
                weights[indexes[j]] = elems[j]
            
    nums = [nums[i[1]] for i in weights]
        
    return ' '.join(nums)def order_weight(strng):
    if strng == "":
        return ""
    nums = strng.split(' ')
    weights = []
    for i in range(0, len(nums)):
        weight = 0
        for ch in nums[i]:
            weight += int(ch)
        weights.append((weight, i))
    weights.sort(key=lambda x: x[0])
    for i in range(0, len(weights)):
        indexes = []
        for  j in range(0, len(weights)):
            if weights[i][0] == weights[j][0]:
                indexes.append(j)
        
        if len(indexes) > 1:
            elems = [weights[i] for i in indexes]
            elems.sort(key=lambda x: nums[x[1]])
            
            index = 0
            for j in range(0, len(indexes)):
                weights[indexes[j]] = elems[j]
            
    nums = [nums[i[1]] for i in weights]
        
    return ' '.join(nums)

def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):
        if i < len(ar) - 1 and \
        (ar[i] + 1 == ar[i+1] or \
         ar[i] - 1 == ar[i+1]):
            count += 1
    return count    

def increment_string(strng):

    strngl = list(strng)
    raw_dgt = []

    while strngl:
        ch = strngl.pop()
        if not ch.isdigit():
            strngl.append(ch)
            break
        raw_dgt.append(ch)

    raw_dgt.reverse()
    dgt, z = "", 0
    z_flag = False

    for ch in raw_dgt:
        if not z_flag and ch == '0':
            z+=1
        else:
            z_flag = True
            dgt += ch
    del raw_dgt

    pr_len = len(dgt)
    dgt = str(int(dgt) + 1) if pr_len > 0 else '1'
    z -= (len(dgt) - pr_len)

    return ''.join(strngl) + ''.join(['0' for x in range(0, z)]) + dgt

def pick_peaks(arr):
    pos, peaks = [], []
    prev, predicted = 0, None
    for i in range(1, len(arr)):
        if arr[i] > arr[prev]:
            predicted = i
        elif predicted is not None and arr[i] < arr[prev]:
            pos.append(predicted)
            peaks.append(arr[predicted])
            predicted = None
        prev = i
    return {"pos" : pos, "peaks" : peaks}

def snail(snail_map):
    res = []
    n = len(snail_map)
    if n == 1:
        return snail_map[0]
    dirs = {
        0.25 : (0, 1),
        0.5 : (1, 0),
        0.75 : (0, -1),
        0 : (-1, 0)
    }
    been = {}
    dir = 1
    i, j = 0, 0
    for _ in range(0, n**2):
        curr_dir = dirs[(dir / 4) - int(dir / 4)]
        if (i == 0 and j == (n-1)) or \
        (i == (n-1) and j == (n-1)) or \
        (i == (n-1) and j == 0) or \
        been.get((i + curr_dir[0], j + curr_dir[1])) != None:
            dir += 1
            curr_dir = dirs[(dir / 4) - int(dir / 4)]

        if (i + curr_dir[0] < n and i >= 0) or \
        (j + curr_dir[1] < n and j >= 0) and \
        been.get((i + curr_dir[0], j + curr_dir[1])) == None:
            been[(i,j)] = True
            res.append(snail_map[i][j])
            i += curr_dir[0]
            j += curr_dir[1]
    return res

def loop_size(node):
    curr = node
    distance = 0
    been = {}
    been [curr] = distance
    while(True):
        curr = curr.next
        distance += 1
        if been.get(curr) != None:
            return distance - been[curr]
        been[curr] = distance

def score(dice):
    sc = 0
    dict = {i : 0 for i in dice}
    for i in dice:
        dict[i] += 1
    
    for i, j in dict.items():
        if j >= 3:
            sc += (i * 100) if i != 1 else 1000
            dict[i] -= 3
    
    if 5 in dict.keys():
        sc += dict[5] * 50
    
    if 1 in dict.keys():
        sc += dict[1] * 100
    
    return sc

def tower_builder(n_floors, block_size):
    w, h = block_size
    res = []
    max = w + (2 * w) * (n_floors - 1)
    for n in range(w, (max + w), 2*w):
        for j in range(0, h):
            diff = (max - n) // 2
            str = ' ' * diff + '*' * n + ' ' * diff
            res.append(str)
    return res

def tower_builder(n_floors):
    res = []
    max = 2 * (n_floors - 1) + 1
    for n in range(1, (max + 1), 2):
        diff = (max // 2) - (n // 2)
        str = ' ' * diff + '*' * n + ' ' * diff
        res.append(str)
    return res

 def sum_dig_pow(a, b):
    res = []
    for i in range(a, b + 1):
        dg_lst = [int(d) for d in str(i)]
        sum = 0
        num = 1
        for d in dg_lst:
            sum += d ** num
            num += 1
        if sum == i:
            res.append(i)
    return res

def order(sentence):
  if sentence == "":
      return ""
  str_lst = sentence.split(' ')
  dict = {}
  
  for i in str_lst:
    h = ''.join(filter(lambda x: x.isdigit(), i))
    dict[h] = i
  
  return " ".join([dict[str(x)] for x in range(1, len(str_lst) + 1)])

def find_nb(m):
    sum = 0
    n = 1
    while(True):
        sum += n ** 3
        if sum == m:
            return n
        elif sum > m:
            return -1
        n += 1

def in_array(array1, array2):
    res = []
    for i in array1:
        for j in array2:
            if j.find(i) != -1:
                res.append(i)
                break
    res.sort()
    return list(dict.fromkeys(res))

def anagrams(word, words):
    return [w for w in words if len(word) == len(w) and set(word) == set(w)]

def find_outlier(integers):
    odd = list(map(lambda a: 1 if a % 2 == 0 else 0, integers))
    return integers[odd.index(0)] if odd.count(0) < odd.count(1) else integers[odd.index(1)]

def duplicate_count(text):
    number = 0
    text = text.lower()
    dict = {x : 0 for x in list(text)}
    for ch in text:
        dict[ch] += 1
    for ch in set(text):
        if dict[ch] > 1:
            number += 1
    return number

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def array_diff(a, b): 
    if a == []:
        return a
        
    for elem in b:
        while elem in a:
            a.remove(elem)
    return a

def multiply(a, b):
  return a * b
