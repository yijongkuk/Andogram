const initialState = {
  isLoggedId: localStorage.getItem("jwt")
};

function reducer(state = initialState, action) {
  switch (action.type) {
    default:
    return state;
  }
}

export default reducer;