import { RootState } from "@/store";


export const selectReceiptItemsState = (state: RootState) => state.receiptItems.receiptItems;


export const selectReceiptItemsLoading = (state: RootState) => state.receiptItems.isLoading;

export const selectReceiptItemsError = (state: RootState) => state.receiptItems.error;