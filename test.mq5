
//+------------------------------------------------------------------+
//|  MQL5 script: Print current positions and apply trailing TP      |
//+------------------------------------------------------------------+
#property script_show_inputs
input double TrailStep = 10.0; // Trail step in points

#include <Trade\Trade.mqh>
CTrade trade;

void OnStart()
  {
   Print("--- Current Positions Detail ---");
   int total = PositionsTotal();
   for(int i=0;i<total;i++)
     {
      ulong ticket = PositionGetTicket(i);
      if(!PositionSelectByTicket(ticket))
         continue;

      string symbol   = (string)PositionGetString(POSITION_SYMBOL);
      ENUM_POSITION_TYPE type = (ENUM_POSITION_TYPE)PositionGetInteger(POSITION_TYPE);
      double   volume = PositionGetDouble(POSITION_VOLUME);
      double   price  = PositionGetDouble(POSITION_PRICE_OPEN);
      double   sl     = PositionGetDouble(POSITION_SL);
      double   tp     = PositionGetDouble(POSITION_TP);
      double   profit = PositionGetDouble(POSITION_PROFIT);
      string   typeStr = (type==POSITION_TYPE_BUY) ? "BUY" : (type==POSITION_TYPE_SELL) ? "SELL" : "UNKNOWN";

      PrintFormat("Ticket:%I64u Symbol:%s Type:%s Volume:%.2f OpenPrice:%.5f SL:%.5f TP:%.5f Profit:%.2f",
                  ticket, symbol, typeStr, volume, price, sl, tp, profit);

      //--- trailing take‑profit logic
      if(type==POSITION_TYPE_BUY && tp>0)
        {
        double newTP = NormalizeDouble(
            SymbolInfoDouble(symbol, SYMBOL_BID) + TrailStep * _Point,
            (int)SymbolInfoInteger(symbol,SYMBOL_DIGITS));
         if(newTP>tp)
            trade.PositionModify(ticket, sl, newTP);
        }
      else if(type==POSITION_TYPE_SELL && tp>0)
        {
          double newTP = NormalizeDouble(
              SymbolInfoDouble(symbol, SYMBOL_ASK) - TrailStep * _Point,
              (int)SymbolInfoInteger(symbol,SYMBOL_DIGITS));
         if(newTP<tp)
            trade.PositionModify(ticket, sl, newTP);
        }
     }
   Print("--- End of Positions ---");
  }
