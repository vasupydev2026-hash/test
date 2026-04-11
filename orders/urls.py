from django.urls import path
from .import views

urlpatterns = [

        path("invoice/<str:order_code>/", views.download_invoice, name="download_invoice"),
        path('confirm_order/', views.confirm_order, name='confirm_order'),
        path('razorpay-payment/', views.razorpay_payment, name='razorpay_payment'),
        path('razorpay-success/', views.razorpay_payment_success, name='razorpay_payment_success'),
        path('my-orders/', views.order_history, name='order_history'),
        path('order-detail/<str:order_code>/', views.order_detail, name='order_detail'),
        path("item/<int:item_id>/cancel/", views.cancel_order_item, name="cancel_order_item"),
        path("item/<int:item_id>/return/", views.item_issue, name="item_issue"),
        path("active-item/<int:item_id>/", views.load_active_item, name="load_active_item"),

        path("active-item/<int:item_id>/", views.active_item_partial, name="active_item"),

        path(
                "item/<int:item_id>/cancel/",
                views.cancel_order_item,
                name="cancel_order_item"
        ),
        path('item/<int:item_id>/track/', views.track_order_item, name='track_order_item'),
        path("success/", views.order_success, name="order_success"),
        path(
            "place-confirm-order/",
            views.place_confirm_order,
            name="place_confirm_order"
        ),
        # orders/urls.py
        # path("ship/<int:order_id>/", views.ship_order_view, name="ship_order"),
        path("returns/", views.returns_list, name="returns_list"),
        path("returns/<int:return_id>/", views.return_detail, name="return_detail"),
        path("returns/<int:return_id>/approve/", views.approve_return, name="approve_return"),
        path("returns/<int:return_id>/refund/", views.refund_return, name="refund_return"),

        path(
                "retry-payment/<int:order_id>/",
                views.retry_payment,
                name="retry_payment"
        ),

        path(
                "payment-failed/<int:order_id>/",
                views.payment_failed_page,
                name="payment_failed_page"
        ),


]