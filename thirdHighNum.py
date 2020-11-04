"""Ganesh's lucky number is 3.
He works as an accountant in a company.
He likes to know the third highest salary among all the employees.

You will be given an array of salaries salary[].
You need to help Ganesh to find the third highest salary (distinct).

NOTE: Salary is in lakhs per annum.

Input Format:
-------------
Line-1: An integer N, number of employees
Line-2: N space separated integers 

Output Format:
--------------
Print an integer, third highest salary.
"""
n=int(input())
sal=[int(x) for x in input().split()]
sal.sort()
sal=list(dict.fromkeys(sal))
print(sal[-3])
