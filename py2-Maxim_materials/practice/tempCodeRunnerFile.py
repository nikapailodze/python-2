c.execute("INSERT INTO employees VALUES (:first, :last ,:pay)", {'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay,})
