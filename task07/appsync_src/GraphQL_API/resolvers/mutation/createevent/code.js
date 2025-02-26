import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';


export function request(ctx) {
	const key = {id: util.autoId()}
	const item = {...ctx.arguments}
	return ddb.put({key, item})
}

export function response(ctx) {
	return ctx.result;
}
