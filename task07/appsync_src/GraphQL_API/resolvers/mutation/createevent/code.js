import { utils } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb'


export function request(ctx) {
    return ddb.put({
		key: ctx.args.input,
		item: "TEST"
	});
}

export function response(ctx) {
    // Update with response logic
    return ctx.result;
}
