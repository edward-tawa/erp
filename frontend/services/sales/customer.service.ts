import api from "@/services/api";
import { Customer, CreateCustomerRequest, CreateCustomerResponse } from "@/types/sales/customer.types";

const customerService = {
    createCustomer: async (customer: CreateCustomerRequest): Promise<CreateCustomerResponse> => {
        const response = await api.post<CreateCustomerResponse>("/customers", customer);
        return response.data;
    },

    getCustomer: async (id: number): Promise<Customer> => {
        const response = await api.get<Customer>(`/customers/${id}`);
        return response.data;
    },

    updateCustomer: async (id: number, customer: CreateCustomerRequest): Promise<Customer> => {
        const response = await api.put<Customer>(`/customers/${id}`, customer);
        return response.data;
    },

    deleteCustomer: async (id: number): Promise<void> => {
        await api.delete(`/customers/${id}`);
    },
}

export default customerService;