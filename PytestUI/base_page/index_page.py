'''
    学校首页页面对象
'''
import allure
from VAR.URL import homepage
from base_key.keyword import Keys


class IndexPage(Keys):
    # url
    url = homepage

    # 页面元素
    student_button = ('link text', '招生就业')
    student_choose = ('link text', '招生')
    course_button = ('link text', '教学科研')
    course_choose = ('link text', '教学')


    # (页面业务,点击招生)
    def student(self, txt):
        with allure.step(f'流程路径为{__file__}'):
            pass
        self.get_url(IndexPage.url)
        self.move_to(IndexPage.student_button[0],IndexPage.student_button[1])
        self.click(IndexPage.student_choose[0],IndexPage.student_choose[1])


    # (页面业务,点击教学)
    def course(self):
        with allure.step(f'流程路径为{__file__}'):
            pass
        self.get_url(IndexPage.url)
        self.move_to(IndexPage.course_button[0],IndexPage.course_button[1])
        self.click(IndexPage.course_choose[0],IndexPage.course_choose[1])
