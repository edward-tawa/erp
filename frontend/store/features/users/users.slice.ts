import { User } from "@/types/users/user.types";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface UsersState {
    users: User[];
    isLoading: boolean;
    isError: boolean | null
}

const initialState: UsersState = {
    users: [],
    isLoading: false,
    isError: false,
}
const usersSlice = createSlice({
    name: "users",
    initialState,
    reducers: {
        setUsers: (state, action: PayloadAction<User[]>) => {
            state.users = action.payload;
        }
    }

})


export const { setUsers } = usersSlice.actions;
export default usersSlice.reducer;