select T.DateTrans as 'Date      ',T.Payee,
lpad(format(-T.Amount,2),8,'       ') as 'Cost   '
from Transactions as T
where T.Category = (Select Id from Categories where Name = "Charitable")
   and Year(T.DateTrans) = 2010
order by T.DateTrans;


select format(SUM(-T.Amount),2) As 'Total Contribution'
from Transactions as T
where T.Category = (Select Id from Categories where Name = "Charitable")
   and Year(T.DateTrans) = 2010
