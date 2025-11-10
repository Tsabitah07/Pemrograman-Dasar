import math
from datetime import datetime

def log_error(exc):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] {exc.__class__.__name__}: {exc}\n'
    with open('error.log', 'a', encoding='utf-8') as f:
        f.write(line)

def run_operations(operations):
    results = []
    for item in operations:
        op = item[0]
        args = item[1:]
        try:
            if op == 'divide':
                a, b = args
                # allow numeric strings too
                a = float(a)
                b = float(b)
                result = a / b
            elif op == 'sqrt':
                (x,) = args
                x = float(x)
                if x < 0:
                    raise ValueError('cannot take sqrt of negative number')
                result = math.sqrt(x)
            elif op == 'to_int':
                (x,) = args
                result = int(x)
            elif op == 'to_float':
                (x,) = args
                result = float(x)
            else:
                raise NotImplementedError(f'unknown operation: {op}')
        except Exception as e:
            log_error(e)
            results.append(None)
        else:
            results.append(result)
    return results

if __name__ == '__main__':
    ops = [
        ('divide', 10, 2),
        ('divide', 5, 0),           # ZeroDivisionError
        ('sqrt', 16),
        ('sqrt', -9),               # ValueError
        ('to_int', '123'),
        ('to_int', 'abc'),          # ValueError
        ('to_float', '12.34'),
        ('to_float', 'not-a-num'),  # ValueError
        ('divide', '100', '20'),
    ]

    res = run_operations(ops)
    for i, r in enumerate(res):
        print(f'\nOp {i}:', 'error' if r is None else r)