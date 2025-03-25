import faker
import argparse

def generate_fake_data(count=1):
    fake = faker.Faker()
    for _ in range(count):
        print(f'Name: {fake.name()}')
        print(f'Address: {fake.address()}')
        print(f'Email: {fake.email()}')
        print(f'Phone Number: {fake.phone_number()}')
        print('-' * 40)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Fake Name and Address Data')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of fake data to generate')
    args = parser.parse_args()
    generate_fake_data(args.number)
    