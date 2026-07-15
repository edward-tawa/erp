import { RootState } from "@/store";


export const selectReceiptItemState = (state: RootState) => state.receiptItem.receiptItem;

export const selectReceiptItemLoading = (state: RootState) => state.receiptItem.isLoading;

export const selectReceiptItemError = (state: RootState) => state.receiptItem.error;