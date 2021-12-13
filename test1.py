path = 'C:/Users/shuf4/practice1/source.csv' 

with open(path, mode='w', encoding='utf-8') as f:
    l_strip = [s.strip() for s in f.readlines()]
    f.write('\n'.join(l_strip))