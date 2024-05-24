class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        return self.count

# Testing the CountedIterator
def main():
    # Instantiate a CountedIterator object using a list
    my_list = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(my_list)

    # Iterate over items
    try:
        while True:
            item = next(counted_iter)
            print(item)
    except StopIteration as e:
        print(e)

    # Print the number of items fetched
    print("Count:", counted_iter.get_count())

if __name__ == "__main__":
    main()
