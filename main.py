# This is a sample Python script.
import index as anc
import Camera as cm
import CreateExcel as excel
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    today = date.today()
    print_hi('PyCharm')
    urls =  cm.CameraInput(today, 203, 4);
    # urls = [];
    # url1 = "E:/Test/2022-04-21/203/1.png";
    # url2 = "E:/Test/2022-04-21/203/2.png";
    # url3 = "E:/Test/2022-04-21/203/3.png";
    # url4 = "E:/Test/2022-04-21/203/4.png";
    # urls.append(url1)
    # urls.append(url2)
    # urls.append(url3)
    # urls.append(url4)
    persons = anc.readImg(urls)
    excel.export_Excel(persons,today)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
