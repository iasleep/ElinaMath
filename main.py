import argparse
import random

parser = argparse.ArgumentParser(description='Process Max value, num of primers and num of actions')
parser.add_argument('max', type=int, help='Maximum value')
parser.add_argument('num', type=int, help='Number of primers')
parser.add_argument('actions', type=int, help='Number of actions')


def random_action():
    some_int = random.randint(1, 20)
    if some_int < 10: return '+'
    else: return '-'


def primery(max, num, actions):
    list_primers = []
    for i in range(num):
        primer = f'{random.randint(1, int(max))}'
        last_rezult = int(primer)
        for action in range(actions):
            bad_rezult = True
            while bad_rezult:
                next_chislo = random.randint(1, int(max))
                next_action = random_action()
                if next_action == '+':
                    rezult = last_rezult + next_chislo
                    if rezult < int(max):
                        primer = f'{primer}+{next_chislo}'
                        last_rezult = rezult
                        bad_rezult = False

                else:
                    rezult = last_rezult - next_chislo
                    if rezult > 0:
                        primer = f'{primer}-{next_chislo}'
                        last_rezult = rezult
                        bad_rezult = False
        primer = f'{primer}='
        list_primers.append(primer)
    return list_primers


if __name__ == '__main__':
    args = parser.parse_args()
    for_print = primery(args.max, args.num, args.actions)
    for primer in for_print:
        print(primer)

