from a import getDistance

# TODO: Prepare actual tests for the task
tests = [
    {
        'args': {
            'graph': None,
            'destNode': 1
        },
        'expected': 0
    },
    {
        'args': {
            'graph': None,
            'destNode': 1
        },
        'expected': 1
    }
]

print(f'Will execute {len(tests)} tests')

successful = 0
for i, test in enumerate(tests):
    if getDistance(**test['args']) == test['expected']:
        print(f'Test {i + 1}: passed')
        successful += 1
    else:
        print(f'Test {i + 1}: failed')
        print('   Arguments:')
        for key, value in test['args'].items():
            print(f'    - {key}: {value}')
        print(f'   Expected result: {test["expected"]}\n')

print(f'{successful} out of {len(tests)} ({successful/len(tests)*100:.1f}%) tests passed')
