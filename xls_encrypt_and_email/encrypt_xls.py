import jpype
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

jvm_path = jpype.get_default_jvm_path()
jxcell_path = os.path.join(project_dir, 'lib/jxcell.jar')


def encrypt(urls, passwd):
    jpype.startJVM(jvm_path, '-ea', '-Djava.class.path=' + jxcell_path)
    view = jpype.JClass('com.jxcell.View')
    m_view = view()
    for url in urls:
        m_view.read(url)
        m_view.write(url, passwd)
    return urls


if __name__ == '__main__':
    encrypt(['./test.xls'], '123')
