import os

from SVM.perform_svm import __svm__


def __svm_main__(__symbol_name__):
    _symbol_list_ = []
    _price_list_ = []

    __interval__ = 5
    symbol_list = ["AAPL", "GOOGL", "INTC", "FB", "TSLA", "NFLX", "YHOO", "AMZN", "MSFT"]

    print("Process " + __symbol_name__ + "...")
    __list__ = []
    __list__ = __svm__(__symbol_name__, __interval__)
    print(__symbol_name__)
    _symbol_list_.append(__symbol_name__)
    print(__interval__)
    print(__list__)
    _price_list_.append(__list__)
    print("Complete " + __symbol_name__ + ".")

    # __log_file__ = "Log/" + str(datetime.date.today()) + "_log.csv"
    # with open(__log_file__, 'wb') as __csv_file_Write__:
    #     fieldnames = ['Symbol', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5']
    #     writer = csv.DictWriter(__csv_file_Write__, fieldnames=fieldnames)
    #
    #     count = 0
    #     for i in range(0, len(_price_list_)):
    #         writer.writerow(
    #             {
    #                 'Symbol': _symbol_list_[i],
    #                 'Day1': _price_list_[i][0],
    #                 'Day2': _price_list_[i][1],
    #                 'Day3': _price_list_[i][2],
    #                 'Day4': _price_list_[i][3],
    #                 'Day5': _price_list_[i][4],
    #             }
    #         )
    return _price_list_
    os.remove("temp.csv")
