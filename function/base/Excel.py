# conding:utf-8
import xlrd
import unittest
import ddt

class ExcelUtil(object):
    def __init__(self):
        excelPath = "D:\\youngmaker_auto\\data\\RanzhiAutoCases.xlsx"
        sheetName = "login"
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

    def next(self):
        datalist = []
        for line in range(1, self.rowNum):
            row = self.table.row_values(line)
            if row:
                datalist.append(row)
        return datalist

if __name__ == "__main__":
    a = ExcelUtil()
    p = a.next()
    print(p)

    import ddt
    @ddt.ddt
    class Test(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        @ddt.data(*p)
        def test_brian(self, data):
            print("username", data[1])
            print("password", data[2])

    unittest.main()