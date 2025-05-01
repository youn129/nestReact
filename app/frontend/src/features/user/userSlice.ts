import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface UserState {
  name: string;
}

const initialState: UserState = {
  name: "Kim",
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    setUserName: (state, action: PayloadAction<string>) => {
      state.name = action.payload;
    },
  },
});

export const { setUserName } = userSlice.actions;
export default userSlice.reducer;
