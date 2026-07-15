import { RootState } from "@/store";


export const selectSalesOrderItemState = (state: RootState) => state.salesOrderItem.salesOrderItem;

export const selectSalesOrderItemLoading = (state: RootState) => state.salesOrderItem.isLoading;

export const selectSalesOrderItemError = (state: RootState) => state.salesOrderItem.error;