"""在验证payment_status是否是ST_PP_COMPLETED后，判断是否已经付款。
如果已经付款，则将order.paid设置为True"""
from mysite import models
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order_id = ipn_obj.invoice.split('-')[-1]
        order = models.Order.objects.get(id = order_id)
        order.paid = True
        order.save()
        print('付款完成。')
#把函数注册到接收此信号的处理函数中
valid_ipn_received.connect(payment_notification)
