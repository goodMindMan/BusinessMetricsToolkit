import partnership.account_types.assets as a
import partnership.account_types.capital as c
import partnership.general_journal as j


mc1 = a.Cash(101, 'mc1')

cp1 = c.Equity(301, 'cp1')

entry1 = j.Journaling()
entry1.two_line_entry('2020-10-3', mc1, cp1, 100.0)

