from customer import Customer
import random
import copy


class Lottery():
    def __init__(self):
        #self.winning_lottery = [random.randint(1, 9) for x in range(0, 6)]
        self.winning_lottery = [8,4,3,4,6,9]
        self.list_of_customers = list()

    def buyTickets(self, input_customer_list):
        for i in input_customer_list:
            self.list_of_customers.append(Customer(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))

    def pickLottery(self):
        print("Winning Lottery Number:", self.winning_lottery)
        winners_list = []

        for i in self.list_of_customers:
            temp_number_list = copy.copy(i.customer_info['lotteryNumber'])
            matching_counter = 0
            copy_win_lott = copy.copy(self.winning_lottery)

            for n in range(0, 6):
                if temp_number_list[n] in copy_win_lott:
                    copy_win_lott.remove(temp_number_list[n])
                    matching_counter += 1
            if matching_counter == 4:
                winners_list.append(f"{i.customer_info['name']} have won 10000$")
            elif matching_counter == 5:
                winners_list.append(f"{i.customer_info['name']} have won 1000000$")
            elif matching_counter == 6:
                winners_list.append(f"{i.customer_info['name']} have won 100000000$")
            else:
                pass
                # print("you have won google pay scratch card! - Better luck next time!")

        return winners_list


# input_customers_list = [[648325, 'Sasidaran', 20, 4, 3, 4, 8, 6, 4],[135952, 'sasi2', 12, 4, 3, 4, 8, 6, 4]]
# input_customers_list = [
#     [648325, 'Sasidaran', 20, 1, 1, 1, 2, 2, 2],
#     [135952, 'sasi2', 12, 4, 3, 4, 3, 4, 4],
#     [976221, 'sasi1', 47, 3, 3, 3, 3, 3, 4],
#     [682742, 'anand', 25, 6, 6, 6, 8, 6, 6],
#     [842965, 'anand1', 57, 8, 8, 8, 8, 7, 7],
#     [112752, 'anand2', 8, 8, 7, 7, 7, 7, 7],
#     [962521, 'sasi3', 52, 9, 9, 9, 9, 9, 9],
# ]

input_customers_list = [
    [648325, 'Sasidaran', 20, 1, 1, 1, 2, 2, 2],
    [135952, 'sasi2', 12, 4, 3, 4, 3, 6, 8],
    [976221, 'sasi1', 47, 3, 9, 4, 3, 8, 6],
    [682742, 'anand', 25, 4, 9, 6, 8, 6, 3],
    [842965, 'anand1', 57, 8, 8, 8, 8, 7, 7],
    [112752, 'anand2', 19, 4, 4, 9, 6, 3, 8],
    [962521, 'sasi3', 52, 9, 3, 6, 8, 9, 4],
]

lottery = Lottery()
lottery.buyTickets(input_customers_list)
winner_list = lottery.pickLottery()
sorted(winner_list)
print(winner_list)
