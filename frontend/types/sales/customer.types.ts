
export interface Customer {
    id: string;
    name: string;
    email: string;
    phoneNumber: string;
    address: string;
    createdAt: string;
    updatedAt?: string;
}


export interface CreateCustomerRequest {
    name: string;
    email: string;
    phoneNumber: string;
    address: string;
}

export interface CreateCustomerResponse {
    id: number;
}


export interface GetCustomerRequest {
    id: string;
}



export type GetCustomerResponse = Customer


export type UpdateCustomerRequest = Partial<Customer>;

export type UpdateCustomerResponse = Customer;

export interface DeleteCustomerRequest {
    id: string;
}

export interface DeleteCustomerResponse {
    message: string;
}