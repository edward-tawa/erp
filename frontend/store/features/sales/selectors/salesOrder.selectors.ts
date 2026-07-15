import { RootState } from "@/store";

export const selectSalesOrderState = (state: RootState) => state.salesOrder.salesOrder;

export const selectSalesOrderLoading = (state: RootState) => state.salesOrder.isLoading;

export const selectSalesOrderError = (state: RootState) => state.salesOrder.error;