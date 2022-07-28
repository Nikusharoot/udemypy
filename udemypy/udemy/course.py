from datetime import datetime


class Course:
    def __init__(
        self, id: int, title: str, link: str, coupon_code: str, date_found: datetime
    ):
        """
        Attributes:
            @id: course id
            @title: course title
            @link: course link
            @coupon_code: course discount coupon code
            @date_found: date when the course was scraped
            @link_with_coupon: link containing coupon code
        """
        self.id = id
        self.title = title
        self.link = link
        self.coupon_code = coupon_code
        self.date_found = date_found

    @property
    def link_with_coupon(self):
        return f"{self.link}?couponCode={self.coupon_code}"


class CourseWithStats(Course):
    def __init__(
        self,
        id: int,
        title: str,
        link: str,
        coupon_code: str,
        date_found: datetime,
        discount: int,
        students: str,
        rating: str,
    ):
        """
        Attributes:
            @discount: discount percentage (1 to 100)
            @students: number of students enrolled to the course
            @rating: course rating (from 0 to 5). It's a str value since it needs to be precise
        """
        super().__init__(id, title, link, coupon_code, date_found)
        self.discount = discount
        self.students = students
        self.rating = rating