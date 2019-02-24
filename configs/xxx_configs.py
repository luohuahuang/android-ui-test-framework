import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

ROLE = {'Manager': 'Manager', 'Staff': 'Staff', 'Waiter': 'Waiter'}

ACCOUNT = {'Manager': 'do_not_delete_mgr', 'Staff': 'do_not_delete_staff', 'Waiter': 'do_not_delete_waiter'}
