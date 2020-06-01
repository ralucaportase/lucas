// @flow

type FetchState = {
    data: any,
    loading: boolean,
    loaded: boolean,
    params: any,
    error: ?{ data: string, status: number },
};

type FetchOptions = {
    successStatusCodes: Array<number>,
};

type FetchMethod = (params: any) => Promise<any>;

const initialState = (): FetchState => ({
    data: undefined,
    loading: false,
    loaded: false,
    params: {},
    error: undefined,
});

const defaultOptions = (): FetchOptions => ({
    successStatusCodes: [202],
});

class FetchError extends Error {
    data: string;
    status: number;

    constructor(message: string, data: string, status: number) {
        super(message);
        this.data = data;
        this.status = status;
    }
}

class FetchReducer {
    name: string;
    fetcher: FetchMethod;
    actions: { [string]: string };
    options: FetchOptions;

    constructor(name: string, fetcher: FetchMethod, options: FetchOptions = {}) {
        this.name = name;
        this.fetcher = fetcher;

        this.actions = {
            start: `FETCH/START/${name}`,
            done: `FETCH/DONE/${name}`,
            error: `FETCH/ERROR/${name}`,
        };

        this.options = {
            ...defaultOptions(),
            ...options,
        };
    }

    reducer() {
        return (state: FetchState = initialState(), action: any) => {
            switch (action.type) {
                case this.actions.start:
                    return {
                        ...state,
                        loading: true,
                    };
                case this.actions.done:
                    return {
                        ...state,
                        data: action.payload,
                        loading: false,
                        loaded: true,
                    };
                case this.actions.error:
                    return {
                        ...state,
                        loading: false,
                        loaded: false,
                        error: action.error,
                    };
                default:
                    return state;
            }
        };
    }

    fetch() {
        return (params: any) => (dispatch: any) => {
            dispatch({
                type: this.actions.start,
            });
            return this.fetcher(params)
                .then(({ data, status }) => {
                    if (!this.options.successStatusCodes.includes(status)) {
                        throw new FetchError(
                            `Fetch for ${this.name} returned ${status}`,
                            data,
                            status,
                        );
                    }
                    dispatch({
                        type: this.actions.done,
                        payload: data,
                    });
                })
                .catch((error) => {
                    dispatch({
                        type: this.actions.error,
                        error: {
                            status: error.status,
                            data: error.data,
                        },
                    });
                });
        };
    }
}

export default FetchReducer;
