import {createApi} from "@reduxjs/toolkit/query/react";
import {createBaseQuery} from "../utils/createBaseQuery.ts";
import type {ICity} from "../types/city/ICity.ts";

export const cityApi= createApi({
    reducerPath: 'cityApi',
    baseQuery: createBaseQuery("cities"),
    tagTypes: ['Cities'],
    endpoints: (builder) => ({

        getCities: builder.query<ICity[], void>({
            query: () => {
                return {
                    url: '',
                    method: 'GET',
                }
            },
        }),

    })
});

export const {
    useGetCitiesQuery
} = cityApi;