# Hands-On 10

## State Management Comparison

### React + Redux Toolkit
- Uses a centralized Redux store.
- Async operations handled using createAsyncThunk.
- Selectors help decouple components from store structure.
- Moderate amount of boilerplate.

### Angular + NgRx
- Follows Redux architecture with Actions, Reducers, Effects and Selectors.
- Effects manage API calls.
- Very scalable but has the highest learning curve.

### Vue + Pinia
- Official state management library for Vue.
- Minimal boilerplate.
- Reactive by default.
- Easier to learn than Redux and NgRx.

## Conclusion

Redux Toolkit provides structured state management for React.
NgRx is powerful for large Angular applications.
Pinia is lightweight and integrates naturally with Vue.