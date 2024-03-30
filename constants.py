class DataMapping:
    """Class for mapping the JSON keys to data columns.
    """
    ORDER_CODE = 'data.orderCode'
    ORDER_FULFILLED_BY = 'data.orderFulfilledBy'
    CUSTOMER_ID = 'data.order.customer.id'
    CUSTOMER_POSTCODE = 'data.order.customer.address.postcode'
    DELIVERY_POSTCODE = 'data.order.delivery.postcode'
    DATE_PURCHASED = 'data.order.datePurchased'
    SKU_ID = 'data.order.lines.skuConfig.skuId'
    SKU_QUANTITY = 'data.order.lines.skuConfig.quantity'
    SKY_LINE_ITEM_NO = 'data.order.lines.skuConfig.lineItemNo'
    SKU_SALE_PRICE = 'data.order.lines.skuConfig.salePrice'
    SKU_SHIP_TOTAL = 'data.order.lines.skuConfig.shipTotal'
    LINE_ID = 'data.order.lines.id'
    PRODUCT_ID = 'data.order.lines.product.id'
    SELLER_ID = 'data.order.lines.product.sellerId'
    PRODUCT_TITLE = 'data.order.lines.product.title'
    PAYMENT_METHOD = 'data.order.payment.method'
    PAYMENT_AMOUNT = 'data.order.payment.amount'
    SALES_CHANNEL = 'data.order.salesChannel.code'

    def get_data_mapping(self, data):
        """Get the data with renamed columns.

        Args:
            data (dict) : Key-value pairs that contains the data.

        Returns:
            The dictionary with renamed keys.
        """
        return {
            'orderCode': data[self.ORDER_CODE],
            'orderFulfilledBy': data[self.ORDER_FULFILLED_BY],
            'customer_id': data[self.CUSTOMER_ID],
            'customer_postcode': data[self.CUSTOMER_POSTCODE],
            'delivery_postcode': data[self.DELIVERY_POSTCODE],
            'datePurchased': data[self.DATE_PURCHASED],
            'skuId': data[self.SKU_ID],
            'sku_quantity': data[self.SKU_QUANTITY],
            'sku_lineItemNo': data[self.SKY_LINE_ITEM_NO],
            'sku_salePrice': data[self.SKU_SALE_PRICE],
            'sku_shipTotal': data[self.SKU_SHIP_TOTAL],
            'line_id': data[self.LINE_ID],
            'product_id': data[self.PRODUCT_ID],
            'sellerId': data[self.SELLER_ID],
            'product_title': data[self.PRODUCT_TITLE],
            'payment_method': data[self.PAYMENT_METHOD],
            'payment_amount': data[self.PAYMENT_AMOUNT],
            'salesChannel': data[self.SALES_CHANNEL]
        }
