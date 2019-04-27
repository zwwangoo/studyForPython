import datetime
import xlwt
import os

project_dir = os.path.dirname(os.path.abspath(__file__))


def json_to_xls(from_data, title):
    try:
        filename = xlwt.Workbook()
        sheet = filename.add_sheet("jujia")
        # 设置表标题
        sheet.write_merge(
            0, 1, 0, 17, title,
            xlwt.easyxf(
                'font: bold on; align: wrap on,'
                'vert centre, horiz center',
            ),
        )

        # 一些说明
        sheet.write_merge(2, 2, 0, 4, '24小时预约：预约动作时间-录入时间')
        sheet.write_merge(2, 2, 5, 9, '完成时间2：完成时间-师傅预约时间')
        sheet.write_merge(3, 3, 0, 4, '48小时完成：完成时间-录入时间')
        sheet.write_merge(3, 3, 5, 9, '预约动作时间为操作订单预约当时时间')
        sheet.write_merge(3, 3, 10, 14, '订单数量：' + str(len(from_data)))

        today = datetime.date.today().strftime('%Y%m%d')
        file_path = os.path.join(project_dir, 'xlss', today + title + '.xls')
        filename.save(file_path)
        print(file_path)
        return file_path
    except Exception as e:
        print(str(e))
        return ''


def make_xls():
    file1 = json_to_xls([], '商户工单完成(维修)')
    file2 = json_to_xls([], '商户工单完成(安装)')
    return [file1, file2]
