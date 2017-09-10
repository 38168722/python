#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/8 12:51
# @Author  : Aries
# @Site    : 
# @File    : mysql 查询作业.py
# @Software: PyCharm

# 1、查询所有的课程的名称以及对应的任课老师姓名

select c.cname as "课程名",t.tname as "教师名"
from course c,teacher t
where c.teacher_id=t.tid;

# 2、查询学生表中男女生各有多少人

select gender as "性别",count(1) as "数量" from student group by gender;

# 3、查询物理成绩等于100的学生的姓名

select * from student where sid in (select student_id from score where num=100 and course_id=(select cid from course where cname="物理"));

# 4、查询平均成绩大于八十分的同学的姓名和平均成绩

SELECT sname 姓名,平均成绩 from student RIGHT JOIN (SELECT student_id,avg(num) 平均成绩 from score GROUP BY student_id HAVING avg(num)>80) as A on student.sid=A.student_id;

# 5、查询所有学生的学号，姓名，选课数，总成绩

SELECT  student_id 学号,sname 姓名,COUNT(course_id) 课程数,SUM(num) 总分 FROM score LEFT JOIN student ON score.student_id=student.sid GROUP BY student_id;

# 6、 查询姓李老师的个数

 select count(1) from teacher where tname like "李%";
 select count(1) from teacher where tname regexp "^李";


# 7、 查询没有报李平老师课的学生姓名

SELECT * FROM student WHERE sid not in (SELECT student_id FROM score WHERE course_id in (
SELECT cid FROM course LEFT JOIN teacher ON teacher.tid=course.teacher_id WHERE tname like "李平%"))

# 8、 查询物理课程比生物课程高的学生的学号

select *
from (select *
from course as c left join score as s on c.cid=s.course_id
where c.cname like "生物") as a inner join (select *
from course as c left join score as s on c.cid=s.course_id
where c.cname like "物理") as b on a.student_id=b.student_id
and b.num>a.num;


# 9、 查询没有同时选修物理课程和体育课程的学生姓名

select *
from student
where sid not in (select student_id
from course as c,score as s
where c.cid=s.course_id and c.cname in ("物理","体育"));


# 10、查询挂科超过两门(包括两门)的学生姓名和班级

select class.caption,student.sname,student.gender
from class,student
where student.class_id=class.cid and student.sid in (
select student_id from score where num<60 group by student_id having length(group_concat(course_id))>=3);

#11 、查询选修了所有课程的学生姓名

select *
from student
where sid in (
select student_id from score group by student_id
having count(course_id)=(select count(cid) from course));

# 12、查询李平老师教的课程的所有成绩记录

select s.student_id,c.cname,s.num
from course c,score s
where c.cid=course_id and c.teacher_id=(select tid from teacher where tname like "李平%");

# 13、查询全部学生都选修了的课程号和课程名

SELECT cid,cname FROM score LEFT JOIN course ON course_id=cid GROUP BY cid HAVING COUNT(student_id)=(SELECT COUNT(*)FROM student);


# 14、查询每门课程被选修的次数

select course.cname 课程名,选修次数
from (select course_id,count(student_id) "选修次数" from score group by course_id) as A left join course on A.course_id=course.cid;

# 15、查询之选修了一门课程的学生姓名和学号

select * from student where sid=(select student_id
from score group by student_id having count(course_id)=1);

# 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）

select student.sname,group_concat(score.num)
from score left join student on score.student_id=student.sid group by student.sname order by group_concat(score.num) desc;

# 17、查询平均成绩大于85的学生姓名和平均成绩

select student.sname,avg(score.num) 平均成绩
from score left join student on score.student_id=student.sid group by student.sname having avg(score.num)>85;

# 18、查询生物成绩不及格的学生姓名和对应生物分数

select student.sname,分数
from (select student_id,num 分数
from score where num<60 and course_id=(select cid from course where cname like "生物"))as a left join student on a.student_id=student.sid;

# 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
select student.sname,max(平均成绩)
from (select student_id,avg(num) 平均成绩
from score
where course_id in (select cid from course where teacher_id=(select tid from teacher where tname like "李平%")) group by student_id) as A left join student on A.student_id=student.sid;

# 20、查询每门课程成绩最好的前两名学生姓名


 select score.sid,score.course_id,score.num,T.first_num,T.second_num from score left join
    (
    select
        sid,
        (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0,1) as first_num,
        (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1,1) as second_num
    from
        score as s1
    ) as T
    on score.sid =T.sid
    where score.num <= T.first_num and score.num >= T.second_num


# 21、查询不同课程但成绩相同的学号，课程号，成绩

select DISTINCT s1.course_id,s2.course_id,s1.num,s2.num from score as s1, score as s2 where s1.num = s2.num and s1.course_id != s2.course_id;

# 22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称；

select 课程名,student.sname 学生名
from (select course.cname 课程名,学生id
from (select student_id 学生id,course_id
from score
where course_id in (select cid from course where teacher_id not in (select tid from teacher where tname like "李平%"))) as A left join course on A.course_id=course.cid) as A left join student on A.学生id=student.sid;

# 23、查询所有选修了课程号为1的同学选修过的一门或者多门课程的同学学号和姓名；
select *
from student
where sid in (
select student_id
from score
where course_id=1);

# 24、任课最多的老师中学生单科成绩最高的学生姓名
select student.sname 姓名,成绩
from (select student_id,max(num) "成绩"
from score
where course_id in (select cid
from course
where teacher_id=(select b.教师id
from
(select A.teacher_id 教师id,max(A.count)
from
(select teacher_id,count(1) as count from course group by teacher_id order by count(1) desc) as A) as B))) as A left join student on student.sid=A.student_id;

