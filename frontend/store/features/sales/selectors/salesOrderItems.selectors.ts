import { RootState } from "@/store";



export const selectSalesOrderItemsState = (state: RootState) => state.salesOrderItems.salesOrderItems;

export const selectSalesOrderItemsLoading = (state: RootState) => state.salesOrderItems.isLoading;

export const selectSalesOrderItemsError = (state: RootState) => state.salesOrderItems.error;