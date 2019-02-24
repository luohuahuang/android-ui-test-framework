# -*- coding: utf-8 -*-

from actions.base.base_action import BaseAction

from actions.loginout.loginout_action import LogInOutAction


base = BaseAction()
login = LogInOutAction()

__all__ = ['base', 'login']
