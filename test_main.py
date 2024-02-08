from main import *


def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(40, 5, 2) == 5390
  assert simple_work_calc(15, 3, 2) == 90
  assert simple_work_calc(25, 4, 2) == 617


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(22, 2, 2, lambda n: n) == 96
  assert work_calc(22, 2, 2, lambda n: 2 * n) == 176
  assert work_calc(40, 3, 2, lambda n: n * n) == 4942


def test_compare_work():
  #c>log_b(a)
  def work_fn1(n):
    a = 8
    b = 2
    c = 4
    f = lambda n: n**c
    return work_calc(n, a, b, f)
  #c<log_b(a)
  def work_fn2(n):
    a = 8
    b = 2
    c = 2
    f = lambda n: n**c
  #c=log_b(a))
  def work_fn3(n):
    a=2
    b=2
    c=1
    f=lambda n: n**c

  res = compare_work(work_fn1, work_fn2, work_fn3)
  print(res)


def test_compare_span():
  def span_fn1(n):
    a = 8
    b = 2
    f = lambda n: 1
    return span_calc(n, a, b, f)

  def span_fn2(n):
    a = 8
    b = 2
    f = lambda n: n * n
    return span_calc(n, a, b, f)

  def span_fn3(n):
    a = 8
    b = 2
    f = lambda n: n
    return span_calc(n, a, b, f)

  res = compare_span(span_fn1, span_fn2, span_fn3)
  print(res)


test_compare_span()
test_compare_work()








