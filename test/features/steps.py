# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append('../')
from Commission import Commission

@step(u'Given I have the "([^"]*)" locks, "([^"]*)" stocks, und "([^"]*)" barrels')
def given_i_have_the_group1_locks_group1_stocks_und_group1_barrels(step, locks, stocks, barrels):
    world.stocks = stocks
    world.locks = locks
    world.barrels = barrels

@step(u'When I compute its commission')
def when_i_compute_its_commission(step):
    c = Commission()
    world.commission = c.calcular(int(world.locks),int(world.stocks),int(world.barrels))

@step(u'Then I see the number "([^"]*)"')
def then_i_see_the_number_group1(step, expected):
    assert world.commission == float(expected), "calculada {0}, esperada {1}".format(world.commission,expected)
