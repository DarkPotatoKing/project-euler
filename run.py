import os

try:
    os.system('clear')
    problem = os.environ['PROJECT_EULER_PROBLEM']
    print 'Running Problem {}\n'.format(problem)
    filename = 'problem_{}.py'.format(str(problem).zfill(3))
    command = 'time python {}'.format(filename)
    os.system(command)
except KeyError:
    print 'Error: Please set a PROJECT_EULER_PROBLEM env variable.'
finally:
    os.system('echo')
