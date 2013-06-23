select T.DateTrans as 'Date      ',
format(if(T.SalesTaxAmount>0,T.SalesTaxAmount*0.07375,T.Amount*-0.07375),2)
 As 'Tax  ',
lpad(format(-T.Amount,2),5,'   ') as 'Cost   ',
T.Payee,concat('(',T.Memo,')') as '(Memo)'
from Transactions as T inner join TransTypes as TT on TT.Id = T.Type
where T.SalesTaxAmount >= 0 and Year(T.DateTrans) = 2010
order by T.DateTrans;

select 
SUM(format(if(T.SalesTaxAmount>0,T.SalesTaxAmount*0.07375,T.Amount*-0.07375),2))
 As 'Total Tax'
from Transactions as T inner join TransTypes as TT on TT.Id = T.Type
where T.SalesTaxAmount >= 0 and Year(T.DateTrans) = 2010;
