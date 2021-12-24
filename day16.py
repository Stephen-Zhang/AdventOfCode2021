import requests
import heapq as hq

def get_input():
    cookie = '53616c7465645f5fcf1f6169d2ad8d0fa193bd441fa5c631f3ac041256ace13262aacc9644e6d018b9d30b5fb64e54e6'
    data = requests.get('https://adventofcode.com/2021/day/16/input', cookies=dict(session=cookie)).text[:-1]

#     data = """
# A0016C880162017C3686B18A3D4780
#          """.strip()

    return data


class Operator:
    def __init__(self, version, type_id, body):
        self.version = version
        self.type_id = type_id
        self.remainder = []
        self.subpackets = []

        self.parse_body(body)

    def parse_body(self, body):
        unparsed = [x for x in body]
        length_type = unparsed.pop(0)

        if length_type == '0':
            self.parse_length_type_1(unparsed)
        elif length_type == '1':
            self.parse_length_type_2(unparsed)


    def parse_length_type_1(self, unparsed):
        # next 15 bits is total length of subpacket bits
        subpacket_len = int(''.join(unparsed[:15]), 2)

        self.remainder = unparsed[15+subpacket_len:]

        unparsed = unparsed[15:15+subpacket_len]
        packet = parse_packet(''.join(unparsed))
        self.subpackets.append(packet)

        remainder = packet.remainder
        while len(remainder) > 0:
            subpacket = parse_packet(''.join(remainder))
            self.subpackets.append(subpacket)
            remainder = subpacket.remainder

    def parse_length_type_2(self, unparsed):
        num_subpackets = int(''.join(unparsed[:11]), 2)
        unparsed = unparsed[11:]

        current_packet = 0
        while current_packet < num_subpackets and len(unparsed) != 0:
            packet = parse_packet(''.join(unparsed))
            self.subpackets.append(packet)
            current_packet += 1

            unparsed = packet.remainder
        self.remainder = unparsed

    def evaluate(self):
        if self.type_id == 0:
            return self.sum_subpackets()
        elif self.type_id == 1:
            return self.prod_subpackets()
        elif self.type_id == 2:
            return self.min_subpackets()
        elif self.type_id == 3:
            return self.max_subpackets()
        elif self.type_id == 5:
            return 1 if self.subpackets[0].evaluate() > self.subpackets[1].evaluate() else 0
        elif self.type_id == 6:
            return 1 if self.subpackets[0].evaluate() < self.subpackets[1].evaluate() else 0
        elif self.type_id == 7:
            return 1 if self.subpackets[0].evaluate() == self.subpackets[1].evaluate() else 0
        

    def sum_subpackets(self):
        if len(self.subpackets) == 1:
            return self.subpackets[0].evaluate()

        total = 0
        for sub in self.subpackets:
            total += sub.evaluate()

        return total

    def prod_subpackets(self):
        if len(self.subpackets) == 1:
            return self.subpackets[0].evaluate()

        total = 1
        for sub in self.subpackets:
            total *= sub.evaluate()

        return total

    def min_subpackets(self):
        values = list(map(lambda x: x.evaluate(), self.subpackets))
        return min(values)

    def max_subpackets(self):
        values = list(map(lambda x: x.evaluate(), self.subpackets))
        return max(values)


class Literal:
    def __init__(self, version, type_id, body):
        self.version = version
        self.type_id = type_id
        self.remainder = []
        self.subpackets = []

        self.value = self.parse_body(body)

    def parse_body(self, body):
        value = ''
        unparsed = [x for x in body]
        last_packet = False
        while len(unparsed) > 0:
            first_bit = unparsed.pop(0)
            if first_bit == '0':
                last_packet = True
            value += ''.join(unparsed[0:4])
            unparsed = unparsed[4:]
            if last_packet:
                if not all([v == '0' for v in unparsed]):
                    self.remainder = unparsed
                break

        return int(value, 2)

    def evaluate(self):
        return self.value


def parse_packet(bin_str):
    version = int(bin_str[:3], 2)
    type_id = int(bin_str[3:6], 2)
    body = bin_str[6:]

    if type_id == 4:
        packet = Literal(version, type_id, body)
    else:
        packet = Operator(version, type_id, body)

    return packet

def day16_part1():
    print(f"day16_part1")
    data = get_input()

    b_str = ''
    for num in data:
        b_str += format(int(num, 16), '04b')

    parsed_packet = parse_packet(b_str)

    total = sum_versions(parsed_packet)

    print(total)


def sum_versions(packet):
    total = packet.version
    for p in packet.subpackets:
        total += sum_versions(p)
    return total


def day16_part2():
    print(f"day16_part2")
    data = get_input()

    b_str = ''
    for num in data:
        b_str += format(int(num, 16), '04b')

    parsed_packet = parse_packet(b_str)

    value = parsed_packet.evaluate()
    print(value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day16_part1()
    day16_part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
