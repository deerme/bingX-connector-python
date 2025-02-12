'''
bingX.perpetual.Swap
'''

from bingX import API

class Swap(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
        base_url :  str = None
    ) -> object:
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = base_url or "https://api-swap-rest.bingbon.pro",
            api_type   = "swap"
        )
    
    def server_time(self) -> dict:
        ''' Get Server Time
        https://bingx-api.github.io/docs/swap/base-info.html#get-server-time
        '''
        return self.get("/api/v1/common/server/time")
    
    # ========== MARKET INTERFACE ==========
    from bingX.perpetual.market import (
        contracts,
        latest_price,
        market_depth,
        latest_trade,
        current_funding_rate,
        funding_rate_history,
        kline_data,
        kline_data_history,
        open_positions,
        ticker,
    )

    # ========== ACCOUNT INTERFACE ==========
    from bingX.perpetual.account import (
        balance,
        positions,
    )
    
    # ========== TRADE INTERFACE ==========
    from bingX.perpetual.trade import (
        place_order,
        close_position,
        close_all_positions,
        cancel_order,
        cancel_orders,
        cancel_all_orders,
        unfilled_order_acquisition,
        order_details,
        margin_mode,
        switch_margin_mode,
        leverage,
        switch_leverage,
        force_orders,
        orders_history,
        place_a_stop_order,
        cancel_stop_order,
        stop_orders,
        stop_orders_history,
    )

    # ========== OTHER INTERFACE ==========
    from bingX.perpetual.other import (
        generate_listen_key,
        extend_listen_key,
        delete_listen_key,
    )