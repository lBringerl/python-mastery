def main():
    with open('portfolio.dat', 'r') as f:
        data_lines = f.read().strip().split('\n')
    overall_price = 0
    for line in data_lines:
        _, shares_count, price = line.split()
        shares_count = int(shares_count)
        price = float(price)
        overall_price += price * shares_count
    print('Result: ', overall_price)


if __name__ == '__main__':
    main()
