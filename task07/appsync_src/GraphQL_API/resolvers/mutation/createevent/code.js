import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';


export function request(ctx) {
    //const { id = util.autoId(), ...item } = ctx.args
	return ddb.put({
		key: {id: util.autoId()},
		item: {test: "TEST-ITEM"}
	})
}

export function response(ctx) {
    // Update with response logic
	//return ctx.result;
    return {
		"id": "test-key",
	}
}
